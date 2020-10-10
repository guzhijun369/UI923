这是一个UI自动化框架，内容构成：python+unittest+selenium+ddt，编写人：古城

目录结构说明：

config/ 配置文件目录

basic_config  私人配置参数，url，邮箱账号密码等

globalparam   项目配置文件，配置日志路径、截图路径、报告路径、浏览器、静默模式、数据读取路径等
data/ 数据驱动文件存放路径

img/ 截图存放路径

public/ 各种方法封装

common   一些公共方法

    basepage  Page基类,后面每个page页都需要继承这个基类，可以封装一些每个页面都通用的方法，比如：操作成功弹窗

    datainfo  读取数据文件方法

    get_img   用例失败后自动截图装饰器，图片名称为用例名称+时间

    mongo_utils   连接mongodb

    mysql_utils   连接mysql

    redis_utils   连接redis

    mytest        unittest基类，封装一些每个用例前后都要进行的操作,可以写多个基类，区分场景继承

    pyselenium    selenium方法、定位二次封装，后续有需要其他定位可添加到里面自定义

    sendmail      发送测试报告方法，由于国内邮件服务经常被封，采用了国外的mailgun  smtp

pages  page页面方法类，一个页面一个文件类
report 测试生成数据目录

html_report  测试报告存放路径

log  log日志存放路径
testcase 用例写在这个目录下，每个用例可以配置两个装饰器：DDT、失败截图装饰器

run 框架入口，包含log初始化、生成测试报告(报告文件是特制的)、配置运行指定单个或者全部用例
