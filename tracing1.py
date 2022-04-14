from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from hwcounter import Timer, count, count_end
import time
import sys

from time import perf_counter, perf_counter_ns, sleep



provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)


tracer = trace.get_tracer(__name__)
for i in range(1000):

    tic = time.perf_counter_ns()
    start = count()

    parent_span = tracer.start_as_current_span("foo")

    parent_span.end()
    end = count_end()
    toc = time.perf_counter_ns()
    elapsed = end - start
    elapsed_time = "{:.4f}".format((toc - tic) / 1000000)
    # print(f'elapsed cycles: {elapsed}')
    sys.stderr.write("\r%d , %s" %(elapsed,elapsed_time))