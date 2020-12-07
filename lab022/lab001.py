from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, DataTypes
from pyflink.table.descriptors import Schema, OldCsv, FileSystem
from pyflink.table.udf import udf

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

t_env = StreamTableEnvironment.create(env)
t_env.get_config().get_configuration().set_string("taskmanager.memory.task.off-heap.size","80m")

add = udf(lambda i, j: i + j, [DataTypes.BIGINT(), DataTypes.BIGINT()], DataTypes.BIGINT())

t_env.register_function("add", add)

t_env.connect(FileSystem().path('/tmp/input')) \
    .with_format(OldCsv()
                 .field('a', DataTypes.BIGINT())
                 .field('b', DataTypes.BIGINT())) \
    .with_schema(Schema()
                 .field('a', DataTypes.BIGINT())
                 .field('b', DataTypes.BIGINT())) \
    .create_temporary_table('mySource')

t_env.connect(FileSystem().path('/tmp/output')) \
    .with_format(OldCsv()
                 .field('sum', DataTypes.BIGINT())) \
    .with_schema(Schema()
                 .field('sum', DataTypes.BIGINT())) \
    .create_temporary_table('mySink')

t_env.from_path('mySource') \
    .select("add(a, b)") \
    .insert_into('mySink')

t_env.execute("tutorial_job")
