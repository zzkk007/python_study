"---------------------------------------------------------------"


						微信公众号

"---------------------------------------------------------------"

						厘清概念

1、本课程的目的：

	掌握微信公众号开发的原理

	熟悉微信公众号的基本功能开发

	锻炼阅读文档，对接第三方接口开发的能力


2、先来看看马化腾家又为我们的汉语创造了哪些新词汇：

	公众号
	公众平台
	订阅号
	服务号
	微信认证

	2.1 公众号和公众平台：

		微信账号类型:

			个人号
		
			公众号
				订阅号
				服务号
			
			企业号
	
		公众号：

			微信公众号主要面向名人、政府、媒体、企业等机构推出的合作推广业务。
			在这里可以通过微信渠道将品牌推广给上亿的微信用户，减少宣传成本，提高品牌知名度，
			打造更具影响力的品牌形象。

		公众平台：

			微信公众平台是运营者通过公众号为微信用户提供资讯和服务的平台，
			而公众平台开发接口则是提供服务的基础，开发者在公众平台网站中创建公众号、
			获取接口权限后，可以通过阅读公众平台开发接口文档来帮助开发。

			微信公众平台可以用来注册、管理公众号和企业号。


		公众号与个人号的区别:	

			微信公众号和个人号是完全不同的。

			微信对个人号的定位是普通用户之间的交流和通讯，微信并不鼓励和支持使用个人号进行营销推广
			(微信曾经大规模封杀好友过多的营销个人号）。
					
			而公众号则完全是为品牌推广、信息推送等服务而定制的。
			使用公众号，可以向关注者（即粉丝)群发图文消息，粉丝在对话界面看到消息后，
			可以点击跳转到一个图文页面。公众号还提供关键词自动回复等基础功能，
			以此可以随时、自动的和粉丝进行互动。

			除了这些基础功能之外，更大的区别是，微信针对公众号开放了很多程序接口。
			在这些接口的基础上，可以向粉丝提供更多的服务。此外，认证的服务号还可以申请微信支付。
			粉丝可以使用微信支付向进行付款（订购服务或购买商品）。所有这些，都是个人号不具备的。

			微信公众号的注册几乎是没有门槛的。
			不过针对不同类型的公众号，微信提供的功能不同，资质要求也不一样
		
	2.2 订阅号与服务号:

		公众号类型

			订阅号
				普通订阅号
				认证订阅号
		
			服务号
				普通服务号
				认证订阅号
		
		订阅号：

			主要偏向于为用户传达资讯，（功能类似报纸杂志，为用户提供新闻信息或娱乐趣事），每天可群发1条消息；

			适用人群：个人、媒体、企业、政府或其他组织。


		服务号:

			主要偏向于服务交互（功能类似12315，114，银行，提供绑定信息，服务交互），每月可群发4条消息；

			适用人群：媒体、企业、政府或其他组织。

		微信认证:

			微信认证是微信公众平台为了确保公众帐号的信息的真实性、安全性，
			目前提供给微信公众服务号进行微信认证的服务。

			微信认证后，获得更丰富的高级接口，向用户提供更有价值的个性化服务。
			微信认证后，用户将在微信中看到微信认证特有的标识
			（公众帐号资料中“认证详情”中会展示认证资料、以及微信认证特有的标识，暂不支持取消）。

"---------------------------------------------------------------"

						微信开发原理

	1、被动回复，粉丝发消息，公众号回复消息。

	2、主动告知，公众号主动给粉丝发消息，例如文字、语音、图文。

	3、内嵌网页，利用内嵌网页链接跳转到网页的形式，向粉丝展示信息内容，或者实现复杂的交互业务逻辑。

	4、明确需求：

		公众号主要通过

			公众号消息会话
			公众号内网页

		来为用户提供服务的。

		公众号消息会话：
			公众号是以微信用户的一个联系人形式存在的，消息会话是公众号与用户交互的基础。

		公众号内网页:
			许多复杂的业务场景，需要通过网页形式来提供服务。

	
	5、公众平台预定义功能：
		
		被动回复——接收粉丝消息并回复

		主动告知——主动给粉丝发消息

		内嵌网页——嵌入网页链接，跳转到网页展现


	6、不给力，满足不了:

		设想两个场景：

		公众号的消息自动回复想做的智能一些，类似于iphone的Siri，
		例如粉丝发送“今天的北京天气”到公众号，回复粉丝信息时要按照特定时间特定城市给予反馈;

		公众号内嵌的网页需要获取浏览用户的微信头像、昵称、当前定位等信息。

		以上两个场景，均无法在公众平台的预定义功能设置中通过配置完成。

		怎么办？


	7 、无扩展应用模型:

		公众号消息会话：

						发送消息
			微信客户端 -----------> 微信服务器
					   <----------- 
				    	回复消息

		公众号内网页:

						发送请求
			微信客户端  -----------> 网页服务器
						<-----------
						返回网页


	8、有扩展应用模型：

		公众号消息会话：

						发送消息            转发消息
			微信客户端 --------> 微信服务器 ----------> 开发者服务器
					   <--------            <----------
						回复消息             返回响应消息

		公众号内网页：

						发送消息             寻求用户信息
			微信客户端 --------> 网页服务器 ----------> 微信服务器
					   <--------            <----------
						返回网页             返回用户信息

	9、公众号接口：

		公众号消息会话：

			目前公众号内主要有这样几类消息服务的类型，分别用于不同的场景。

			群发消息：

				公众号可以以一定频次（订阅号为每天1次，服务号为每月4次），向用户群发消息，
				包括文字消息、图文消息、图片、视频、语音等。
			
			被动回复消息：

				在用户给公众号发消息后，微信服务器会将消息发到开发者预先在开发者中心设置的服务器地址
				（开发者需要进行消息真实性验证），公众号可以在5秒内做出回复，可以回复一个消息，
				也可以回复命令告诉微信服务器这条消息暂不回复。
				被动回复消息可以设置加密（在公众平台官网的开发者中心处设置，
				设置后，按照消息加解密文档来进行处理。
				其他3种消息的调用因为是API调用而不是对请求的返回，所以不需要加解密）。

			客服消息：

				在用户给公众号发消息后的48小时内，公众号可以给用户发送不限数量的消息，
				主要用于客服场景。用户的行为会触发事件推送，某些事件推送是支持公众号据此发送客服消息的，
				详见微信推送消息与事件说明文档。

			模板消息

				在需要对用户发送服务通知（如刷卡提醒、服务预约成功通知等）时，
				公众号可以用特定内容模板，主动向用户发送消息。	

		公众号内网页：

			对于公众号内网页，提供以下场景接口：
			
				网页授权获取用户基本信息
					
					通过该接口，可以获取用户的基本信息

				微信JS-SDK

					是开发者在网页上通过JavaScript代码使用微信原生功能的工具包，
					开发者可以使用它在网页上录制和播放微信语音、监听微信分享、
					上传手机本地图片、拍照等许多能力。

		微信开发者文档：

			微信开发者文档网址 https://mp.weixin.qq.com/wiki/home/index.html


"----------------------------------------------------------------"

						接入微信公众平台

	1、接入微信公众平台

		接入微信公众平台开发，开发者需要按照如下步骤完成：

			填写服务器配置
			验证服务器地址的有效性
			依据接口文档实现业务逻辑


	2、填写服务器配置:

		登录微信公众平台官网后，在公众平台后台管理页面 - 开发者中心页，
		点击“修改配置”按钮，填写服务器地址（URL）、Token和EncodingAESKey，
		其中URL是开发者用来接收微信消息和事件的接口URL。
		Token可由开发者可以任意填写，用作生成签名（该Token会和接口URL中包含的Token进行比对，从而验证安全性）。
		EncodingAESKey由开发者手动填写或随机生成，将用作消息体加解密密钥。

		同时，开发者可选择消息加解密方式：明文模式、兼容模式和安全模式。
		模式的选择与服务器配置在提交后都会立即生效，请开发者谨慎填写及选择。
		加解密方式的默认状态为明文模式，
		选择兼容模式和安全模式需要提前配置好相关加解密代码，详情请参考消息体签名及加解密部分的文档。


		微信公众号接口只支持80接口。

		利用测试平台:

			测试平台登陆地址 http://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login

	3、验证服务器地址的有效性：

		开发者提交信息后，微信服务器将发送GET请求到填写的服务器地址URL上，GET请求携带四个参数：

			参数                   描述

			signature            微信加密签名，signature结合了开发者填写的token参数
								 和请求中的timestamp参数、nonce参数  

			timestamp            时间戳

			nonce                随机数

			echostr              随机字符串

		开发者通过检验signature对请求进行校验。
		若确认此次GET请求来自微信服务器，请原样返回echostr参数内容，则接入生效，成为开发者成功，否则接入失败。

		校验流程：

			1. 将token、timestamp、nonce三个参数进行字典序排序
			2. 将三个参数字符串拼接成一个字符串进行sha1加密
			3. 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信

		
		Python代码实现(以Tornado框架为例)：

			class WechatHandler(tornado.web.RequestHandler):
				"""微信接入口"""
				def get(self):

					"""开发者验证接口"""

					signature = self.get_argumnet("signature","")
					timestamp = self.get_argument("timestamp","")
					nonce = self.get_argument("nonce","")
					echostr = self.get_argument("echostr","")

					tmp = [WECHAT_TOKEN,timestamp,nonce]
					tmp.sort()
					tmp = "".join(temp)
					tmp = hashlib.sha1(tmp).hexdigest()
					if tmp == signature:
						self.write(echostr)
					else:
						self.write("error")

		
"----------------------------------------------------------------"

						公众号接收和发送消息
	
	1、公众号接收与发送消息:

		验证URL有效性成功后即接入生效，成为开发者。
		如果公众号类型为服务号（订阅号只能使用普通消息接口），可以在公众平台网站中申请认证，
		认证成功的服务号将获得众多接口权限，以满足开发者需求。

		此后用户每次向公众号发送消息、或者产生自定义菜单点击事件时，
		开发者填写的服务器配置URL将得到微信服务器推送过来的消息和事件，
		然后开发者可以依据自身业务逻辑进行响应，例如回复消息等。

		用户向公众号发送消息时，公众号方收到的消息发送者是一个OpenID，
		是使用用户微信号加密后的结果，每个用户对每个公众号有一个唯一的OpenID。


	2、接收普通消息：

		当普通微信用户向公众号发消息时，微信服务器将POST消息的XML数据包到开发者填写的URL上。

		微信服务器在五秒内收不到响应会断掉连接，并且重新发起请求，总共重试三次。
		假如服务器无法保证在五秒内处理并回复，可以直接回复空串，
		微信服务器不会对此作任何处理，并且不会发起重试。

		各消息类型的推送使用XML数据包结构，如：


			<xml>
			<ToUserName><![CDATA[gh_866835093fea]]></ToUserName>
			<FromUserName><![CDATA[ogdotwSc_MmEEsJs9-ABZ1QL_4r4]]></FromUserName>
			<CreateTime>1478317060</CreateTime>
			<MsgType><![CDATA[text]]></MsgType>
			<Content><![CDATA[你好]]></Content>
			<MsgId>6349323426230210995</MsgId>
			</xml>

			注意：<![CDATA 与 ]]> 括起来的数据不会被xml解析器解析。

		xmltodict 模块基本用法：

			xmltodict 是一个用来处理xml数据的很方便的模块。包含两个常用方法parse和unparse
			
			1、parse

			xmltodict.parse()方法可以将xml数据转为python中的dict字典数据：

				>>> import xmltodict
				>>> xml_str = """
				... <xml>
				... <ToUserName><![CDATA[gh_866835093fea]]></ToUserName>
				... <FromUserName><![CDATA[ogdotwSc_MmEEsJs9-ABZ1QL_4r4]]></FromUserName>
				... <CreateTime>1478317060</CreateTime>
				... <MsgType><![CDATA[text]]></MsgType>
				... <Content><![CDATA[你好]]></Content>
				... <MsgId>6349323426230210995</MsgId>
				... </xml>
				... """
				>>>
				>>> xml_dict = xmltodict.parse(xml_str)
				>>> type(xml_dict)
					<class 'collections.OrderedDict'>  # 类字典型，可以按照字典方法操作
				>>>
				>>> xml_dict
					OrderedDict([(u'xml', OrderedDict([(u'ToUserName', u'gh_866835093fea'), (u'FromUserName', u'ogdotwSc_MmEEsJs9-ABZ1QL_4r4'), (u'CreateTime', u'1478317060'), (u'MsgType', u'text'), (u'Content', u'\u4f60\u597d'), (u'MsgId', u'6349323426230210995')]))])
			
				>>>
				>>> xml_dict['xml']
					OrderedDict([(u'ToUserName', u'gh_866835093fea'), (u'FromUserName', u'ogdotwSc_MmEEsJs9-ABZ1QL_4r4'), (u'CreateTime', u'1478317060'), (u'MsgType', u'text'), (u'Content', u'\u4f60\u597d'), (u'MsgId', u'6349323426230210995')])
				
				>>>
				>>> for key, val in xml_dict['xml'].items():
					...     print key, "=", val
					... 
					ToUserName = gh_866835093fea
					FromUserName = ogdotwSc_MmEEsJs9-ABZ1QL_4r4
					CreateTime = 1478317060
					MsgType = text
					Content = 你好
					MsgId = 6349323426230210995
			
			2、unparse:

				xmltodict.unparse()方法可以将字典转换为xml字符串：
				
				xml_dict = {

					"xml": {
							
						"ToUserName" : "gh_866835093fea",
						"FromUserName" : "ogdotwSc_MmEEsJs9-ABZ1QL_4r4",
						"CreateTime" : "1478317060",
						"MsgType" : "text",
						"Content" : u"你好",
						"MsgId" : "6349323426230210995",
							}
				}

				>>> xml_str = xmltodict.unparse(xml_dict)
				>>> print xml_str
				<?xml version="1.0" encoding="utf-8"?>
				<xml><FromUserName>ogdotwSc_MmEEsJs9-ABZ1QL_4r4</FromUserName><MsgId>6349323426230210995</MsgId><ToUserName>gh_866835093fea</ToUserName><Content>你好</Content><MsgType>text</MsgType><CreateTime>1478317060</CreateTime></xml>
				>>>
				>>> xml_str = xmltodict.unparse(xml_dict, pretty=True) # pretty表示友好输出
				>>> print xml_str
				<?xml version="1.0" encoding="utf-8"?>
				<xml>
					<FromUserName>ogdotwSc_MmEEsJs9-ABZ1QL_4r4</FromUserName>
					<MsgId>6349323426230210995</MsgId>
					<ToUserName>gh_866835093fea</ToUserName>
				    <Content>你好</Content>
					<MsgType>text</MsgType>
					<CreateTime>1478317060</CreateTime>
					</xml>
				>>>


		普通消息类别:

			1、文本消息
			2、图片消息
			3、语音消息
			4、视频消息
			5、小视频消息
			6、地理位置消息
			7、链接消息
			
		文本消息：

			<xml>
			<ToUserName><![CDATA[toUser]]></ToUserName>
			<FromUserName><![CDATA[fromUser]]></FromUserName> 
			<CreateTime>1348831860</CreateTime>
			<MsgType><![CDATA[text]]></MsgType>
			<Content><![CDATA[this is a test]]></Content>
			<MsgId>1234567890123456</MsgId>
			</xml>


			参数                      描述

			ToUserName                开发者微信好

			FormUserName              发送方的账号(一个OpenID)

			CreateTime                消息创建时间(整型)

			MsgType                   text

			Content                   文本消息的内容

			Msgid                     消息id,64位整型

	3、被动回复消息：

		当用户发送消息给公众号时（或某些特定的用户操作引发的事件推送时），会产生一个POST请求，
		开发者可以在响应包中返回特定XML结构，来对该消息进行响应
		（现支持回复文本、图片、图文、语音、视频、音乐）。
		严格来说，发送被动响应消息其实并不是一种接口，而是对微信服务器发过来消息的一次回复。

		假如服务器无法保证在五秒内处理并回复，必须做出下述回复，这样微信服务器才不会对此作任何处理，
		并且不会发起重试（这种情况下，可以使用客服消息接口进行异步回复），
		否则，将出现严重的错误提示。详见下面说明：

			1.（推荐方式）直接回复success

			2. 直接回复空串（指字节长度为0的空字符串，而不是XML结构体中content字段的内容为空）

			一旦遇到以下情况，微信都会在公众号会话中，向用户下发系统提示“该公众号暂时无法提供服务，
			请稍后再试”：

				开发者在5秒内未回复任何内容
				开发者回复了异常数据，比如JSON数据等

		回复的消息类型:

			文本消息
			图片消息
			语音消息
			视频消息
			音乐消息
			图文消息

		回复文本消息:

			<xml>
			<ToUserName><![CDATA[toUser]]></ToUserName>
			<FromUserName><![CDATA[fromUser]]></FromUserName>
			<CreateTime>12345678</CreateTime>
			<MsgType><![CDATA[text]]></MsgType>
			<Content><![CDATA[你好]]></Content>
			</xml>

		参数              是否必须              描述

		ToUserName         是                  接收方账号(收到的OpenID)

		FormUserName       是                  开发者微信号

		CreateTime         是                  消息创建时间(整型)

		MsgType            是                  text

		Content            是                  回复的消息内容(换行:在content中能够换行，微信客户端就支持换行)


	4、鹦鹉学舌代码实现：

		我们现在来实现一个针对文本消息的收发程序。
		实现的业务逻辑类似与“鹦鹉学舌”，粉丝发什么内容，我们就传回给粉丝什么内容。
		

			#coding:utf-8

			import tornado.web
			import tornado.httpserver
			import tornado.ioloop
			import tornado.options
			import hashlib
			import xmltodict
			import time

			form tornado.web import RequestHandler
			form tornado.options import define,options

			WECHAT_TOKEN = "itcast"

			define("port", default=8080, type=int)

			class WechatHandler(RequestHandler):
				"""微信接入口"""
				def get(self):
					"""开发者验证接口"""
					signature = self.get_argument("signature")
					timestamp = self.get_argument("timestamp")
					nonce = self.get_argument("nonce")
					echostr = self.get_argument("echostr")
					tmp = [WECHAT_TOKEN, timestamp, nonce]
					tmp.sort()
					tmp = "".join(tmp)
					tmp = hashlib.sha1(tmp).hexdigest()
					if tmp == signature:
						self.write(echostr)
					else:
						self.write("error")

				def post(self):
					"""收发消息接口"""
					req_xml = self.request.body
					req = xmltodict.parse(req_xml)['xml']
					if "text" == req.get("MsgType"):
						resp = {
								"ToUserName":req.get("FromUserName", ""),
								"FromUserName":req.get("ToUserName", ""),
								"CreateTime":int(time.time()),
								"MsgType":"text",
								"Content":req.get("Content", "")
						}
					else:
						resp = {
								"ToUserName":req.get("FromUserName", ""),
								"FromUserName":req.get("ToUserName", ""),
								"CreateTime":int(time.time()),
								"MsgType":"text",
								"Content":"I love you, itcast!"
						}
					resp_xml = xmltodict.unparse({"xml":resp})
					self.write(resp_xml)
			

			def main():

				tornado.options.parse_command_line()
				app = tornado.web.Application([
				        (r"/wechat", WeChatHandler),
							        ])
				http_server = tornado.httpserver.HTTPServer(app)
				http_server.listen(options.port)
				tornado.ioloop.IOLoop.current().start()
				
			if __name__ == '__main__':
			    main()


		有趣的表情:

			QQ表情

				实际是字符串转义，如 /::D、/::P 等，仍属于文本信息。

			emoji

				绘文字（日语：絵文字/えもじ emoji）是日本在无线通信中所使用的视觉情感符号，
				绘意指图形，文字则是图形的隐喻，可用来代表多种表情，如笑脸表示笑、蛋糕表示食物等。

				在NTTDoCoMo的i-mode系统电话系统中，绘文字的尺寸是12x12 像素，
				在传送时，一个图形有2个字节。Unicode编码为E63E到E757，而在Shift-JIS编码则是从F89F到F9FC。
				基本的绘文字共有176个符号，在C-HTML4.0的编程语言中，则另增添了76个情感符号。

				最早由栗田穰崇（Shigetaka Kurita）创作，并在日本网络及手机用户中流行。

				自苹果公司发布的iOS 5输入法中加入了emoji后，这种表情符号开始席卷全球，
				目前emoji已被大多数现代计算机系统所兼容的Unicode编码采纳，普遍应用于各种手机短信和社交网络中。

				本质是Unicode字符，也属于文本消息。

			自定表情

				微信的自定义表情不是文本，也不是图片，而是一种不支持的格式，微信未提供处理此消息的接口。
						

		改写代码

			微信发送的请求中会携带签名验证信息（正如验证服务器有效性一章节所示），
			我们需要对收到的请求进行验证是否来自微信服务器，所以在处理请求前都要按照验证算法进行检验。
						

			class WeChatBaseHandler(RequestHandler):
				def prepare(self):
					"""验证请求是否来自微信服务器"""
					signature = self.get_argument("signature")
					timestamp = self.get_argument("timestamp")
					nonce = self.get_argument("nonce")
					tmp = [WECHAT_TOKEN, timestamp, nonce]
					tmp.sort()
					tmp = "".join(tmp)
					tmp = hashlib.sha1(tmp).hexdigest()
					if tmp != signature:
						self.send_error(403) # 若是非法请求，返回403错误

			class WeChatHandler(WeChatBaseHandler):
				"""微信接入接口"""
				def get(self):
					"""开发者验证接口"""
					echostr = self.get_argument("echostr")
					self.write(echostr)

					def post(self):
						req_xml = self.request.body
						req = xmltodict.parse(req_xml)['xml']
						if "text" == req.get("MsgType"):
						resp = {

							"ToUserName":req.get("FromUserName", ""),
							"FromUserName":req.get("ToUserName", ""),
							"CreateTime":int(time.time()),
							"MsgType":"text",
							"Content":req.get("Content", "")
						}
					else:
						resp = {

							"ToUserName":req.get("FromUserName", ""),
							"FromUserName":req.get("ToUserName", ""),
							"CreateTime":int(time.time()),
							"MsgType":"text",
							"Content":"I love you, itcast!"
					}
					resp_xml = xmltodict.unparse({"xml":resp})
					self.write(resp_xml)


	5、接收其他普通消息:

		接收图片消息:

			<xml>
			<ToUserName><![CDATA[toUser]]></ToUserName>
			<FromUserName><![CDATA[fromUser]]></FromUserName>
			<CreateTime>1348831860</CreateTime>
			<MsgType><![CDATA[image]]></MsgType>
			<PicUrl><![CDATA[this is a url]]></PicUrl>
			<MediaId><![CDATA[media_id]]></MediaId>
			<MsgId>1234567890123456</MsgId>
			</xml>

			参数	          描述
			ToUserName	    开发者微信号
			FromUserName	发送方帐号（一个OpenID）
			CreateTime	    消息创建时间 （整型）
			MsgType	        image
			PicUrl	        图片链接
			MediaId	        图片消息媒体id，可以调用多媒体文件下载接口拉取数据。
			MsgId	        消息id，64位整型

		
		接收视频消息:

			<xml>
			<ToUserName><![CDATA[toUser]]></ToUserName>
			<FromUserName><![CDATA[fromUser]]></FromUserName>
			<CreateTime>1357290913</CreateTime>
			<MsgType><![CDATA[video]]></MsgType>
			<MediaId><![CDATA[media_id]]></MediaId>
			<ThumbMediaId><![CDATA[thumb_media_id]]></ThumbMediaId>
			<MsgId>1234567890123456</MsgId>
			</xml>

			参数	         描述
			ToUserName	    开发者微信号
			FromUserName	发送方帐号（一个OpenID）
			CreateTime	    消息创建时间 （整型）
			MsgType	        视频为video
			MediaId	        视频消息媒体id，可以调用多媒体文件下载接口拉取数据。
			ThumbMediaId	视频消息缩略图的媒体id，可以调用多媒体文件下载接口拉取数据。
			MsgId	        消息id，64位整型


		接收小视频消息:

			<xml>
			<ToUserName><![CDATA[toUser]]></ToUserName>
			<FromUserName><![CDATA[fromUser]]></FromUserName>
			<CreateTime>1357290913</CreateTime>
			<MsgType><![CDATA[shortvideo]]></MsgType>
			<MediaId><![CDATA[media_id]]></MediaId>
			<ThumbMediaId><![CDATA[thumb_media_id]]></ThumbMediaId>
			<MsgId>1234567890123456</MsgId>
			</xml>

			参数	         描述
			ToUserName		开发者微信号
			FromUserName	发送方帐号（一个OpenID）
			CreateTime		消息创建时间 （整型）
			MsgType			小视频为shortvideo
			MediaId			视频消息媒体id，可以调用多媒体文件下载接口拉取数据。
			ThumbMediaId	视频消息缩略图的媒体id，可以调用多媒体文件下载接口拉取数据。
			MsgId			消息id，64位整型


		接收语音消息:

			<xml>
			<ToUserName><![CDATA[toUser]]></ToUserName>
			<FromUserName><![CDATA[fromUser]]></FromUserName>
			<CreateTime>1357290913</CreateTime>
			<MsgType><![CDATA[voice]]></MsgType>
			<MediaId><![CDATA[media_id]]></MediaId>
			<Format><![CDATA[Format]]></Format>
			<MsgId>1234567890123456</MsgId>
			</xml>


			参数			描述
			ToUserName		开发者微信号
			FromUserName	发送方帐号（一个OpenID）
			CreateTime		消息创建时间 （整型）
			MsgType			语音为voice
			MediaId			语音消息媒体id，可以调用多媒体文件下载接口拉取数据。
			Format			语音格式，如amr，speex等
			MsgID			消息id，64位整型

			请注意，开通语音识别后，用户每次发送语音给公众号时，
			微信会在推送的语音消息XML数据包中，增加一个Recongnition字段
			（注：由于客户端缓存，开发者开启或者关闭语音识别功能，对新关注者立刻生效，
			对已关注用户需要24小时生效。开发者可以重新关注此帐号进行测试）。
			开启语音识别后的语音XML数据包如下：

				<xml>
				<ToUserName><![CDATA[toUser]]></ToUserName>
				<FromUserName><![CDATA[fromUser]]></FromUserName>
				<CreateTime>1357290913</CreateTime>
				<MsgType><![CDATA[voice]]></MsgType>
				<MediaId><![CDATA[media_id]]></MediaId>
				<Format><![CDATA[Format]]></Format>
				<Recognition><![CDATA[腾讯微信团队]]></Recognition>
				<MsgId>1234567890123456</MsgId>
				</xml>

			多出的字段中，Format为语音格式，一般为amr，Recognition为语音识别结果，使用UTF8编码。
		








"----------------------------------------------------------------"


						微信网页授权						

"----------------------------------------------------------------"

						自定义菜单

"----------------------------------------------------------------"
