from ipykernel.kernelbase import Kernel
from IPython.display import display, HTML
import duckdb
from tabulate import tabulate


def Run_SQL(code):
    code = str(code)+';'
    return duckdb.sql(code)

def rep_code(code):
    return code+code

# https://github.com/bgschiller/postgres_kernel/blob/master/postgres_kernel/kernel.py
def display_data(header, rows):
    d = {
        'data': {
            'text/latex': tabulate(rows, header, tablefmt='latex_booktabs'),
            'text/plain': tabulate(rows, header, tablefmt='simple'),
            'text/html': tabulate(rows, header, tablefmt='html'),
        },
        'metadata': {}
    }
    return d
    # return tabulate(rows, header, tablefmt='html')


class DuckdbKernel(Kernel):
    implementation = 'duckdb'
    implementation_version = '0.1.0'
    language = 'sql'
    language_version = '0.1.0'
    language_info = {
        'name': 'DUCKDB',
        'mimetype': 'text/plain',
        'file_extension': '.sql',
    }
    banner = "duckdb kernel"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:

            try:
                df = Run_SQL(code).df()
                # Run_SQL(code).df().to_json()
                # content = df.to_json()
                
                header = df.columns.tolist()
                rows = df.values.tolist()
                content = display_data(header, rows)
                
                # 标准输出
                # stream_content = {'name': 'stdout', 'text': content}
                # self.send_response(self.iopub_socket, 'stream', stream_content)
                
                # 富文本输出
                self.send_response(self.iopub_socket, 'display_data', content)
            
            except Exception as e:
                content = str(e)
                if "'NoneType' object has no attribute" in content:
                    content = ''
                stream_content = {'name': 'stdout', 'text': content}
                self.send_response(self.iopub_socket, 'stream', stream_content)


        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=DuckdbKernel)
