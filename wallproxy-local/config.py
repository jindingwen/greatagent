# -*- coding: utf-8 -*-
# 是否使用ini作为配置文件，0不使用
ini_config = 1368321848
# 监听ip
listen_ip = '127.0.0.1'
# 监听端口
listen_port = 8086
# 是否使用通配符证书
cert_wildcard = 1
# 更新PAC时也许还没联网，等待tasks_delay秒后才开始更新
tasks_delay = 0
# WEB界面是否对本机也要求认证
web_authlocal = 0
# 登录WEB界面的用户名
web_username = 'admin'
# 登录WEB界面的密码
web_password = 'admin'
# 全局代理
global_proxy = None
# URLFetch参数
fetch_keepalive = 1
check_update = 0

def config():
    Forward, set_dns, set_resolve, set_hosts, check_auth, redirect_https = import_from('util')
    RAW_FORWARD = FORWARD = Forward()
    set_dns('8.8.8.8')
    set_resolve('talk.google.com talkx.l.google.com .youtube.com .facebook.com')
    google_sites = ('.appspot.com', '.google.com', '.google.com.hk', '.googlecode.com', '.googleusercontent.com', '.googlegroups.com', '.google-analytics.com', '.gstatic.com', '.googleapis.com', '.blogger.com', '.ggpht.com')
    google_hosts = 'www.google.com mail.google.com dl.google.com dl-ssl.google.com accounts.google.com appengine.google.com developers.google.com www.android.com developer.android.com android.googlesource.com www.google-analytics.com ssl.google-analytics.com www.gstatic.com ssl.gstatic.com ajax.googleapis.com translate.googleapis.com'
    set_hosts(google_sites, google_hosts)
    set_hosts('www.youtube.com upload.youtube.com', google_hosts)

    from plugins import misc; misc = install('misc', misc)
    PAGE = misc.Page('page.html')

    from plugins import paas; paas = install('paas', paas)
    GAE = paas.GAE(appids=['freegoagent297', 'gfanqiang020-3', 'freegoagent056', 'freegoagent604', 'gfanqiang033-5', 'fgabootstrap002', 'comeforu-upu2b-008', 'freegoagent204', 'gfanqiang014-2', 'freegoagent641', 'freegoagent575', 'freegoagent084', 'freegoagent361', 'freegoagent839', 'freegoagent514', 'freegoagent355', 'freegoagent673', 'freegoagent487', 'freegoagent100', 'freegoagent752', 'gfanqiang016-2', 'freegoagent068', 'deepb163-comeforu-001', 'gfanqiang005-2', 'freegoagent952', 'freegoagent769', 'freegoagent597', 'freegoagent211', 'freegoagent568', 'freegoagent761', 'freegoagent905', 'gfanqiang028-1', 'freegoagent777', 'freegoagent308', 'freegoagent719', 'freegoagent175', 'okp163-comeforu-006', 'freegoagent588', 'freegoagent505', 'freegoagent889', 'freegoagent435', 'freegoagent717', 'freegoagent648', 'freegoagent088', 'gfanqiang003-2', 'freegoagent281', 'freegoagent006', 'freegoagent653', 'ok126-comeforu-001', 'gfanqiang023-7', 'gfanqiang020-5', 'freegoagent135', 'freegoagent853', 'gfanqiang024-0', 'freegoagent051', 'freegoagent224', 'ok126-comeforu-007', 'freegoagent741', 'freegoagent567', 'gfanqiang019-5', 'freegoagent190', 'gfanqiang004-7', 'freegoagent430', 'freegoagent578', 'rest126-comeforu-002', 'fgg163-comeforu-007', 'gfanqiang007-2', 'freegoagent164', 'freegoagent261', 'okp163-comeforu-001', 'qq997-comeforu-003', 'freegoagent935', 'aft126-comeforu-004', 'freegoagent961', 'gfanqiang005-1', 'freegoagent060', 'freegoagent363', 'gfanqiang026-5', 'freegoagent358', 'freegoagent516', 'freegoagent674', 'freegoagent379', 'freegoagent344', 'freegoagent306', 'freegoagent397', 'gfanqiang024-4', 'freegoagent606', 'freegoagent631', 'freegoagent476', 'freegoagent335', 'gfanqiang006-7', 'deepbyeah-comeforu-008', 'gfanqiang005-6', 'freegoagent490', 'freegoagent316', 'fghdis9105z-06', 'freegoagent775', 'freegoagent365', 'freegoagent389', 'freegoagent253', 'freegoagent091', 'freegoagent630', 'gfanqiang036-9', 'freegoagent941', 'freegoagent957', 'freegoagent191', 'gfanqiang007-8', 'gfanqiang031-6', 'freegoagent016', 'gfanqiang013-5', 's-g9085h-06', 'gfanqiang007-7', 'gfanqiang034-0', 'freegoagent633', 'rest126-comeforu-001', 'freegoagent452', 'rest126-comeforu-007', 'freegoagent813', 'freegoagent937', 'freegoagent201', 'freegoagent549', 'freegoagent940', 'x9088-sz-01', 'freegoagent918', 'freegoagent808', 'freegoagent057', 'freegoagent931', 'mhyeah-comeforu-005', 'freegoagent696', 'freegoagent806', 'freegoagent873', 'gfanqiang015-4', 'freegoagent401', 'gfanqiang035-5', 'freegoagent220', 'gfanqiang034-5', 'freegoagent707', 'freegoagent711', 'freegoagent870', 'freegoagent268', 'gfanqiang019-4', 'freegoagent376', 'freegoagent908', 'w519163-comeforu-007', 'freegoagent309', 'freegoagent137', 'deepbyeah-comeforu-003', 'gfanqiang017-1', 'freegoagent545', 'freegoagent742', 'freegoagent252', 'gfanqiang020-2', 'freegoagent572', 'okadm-comeforu-003', 'freegoagent793', 'freegoagent018', 'freegoagent139', 'dz126-comeforu-001', 'gfanqiang008-8', 'freegoagent541', 'mhyeah-comeforu-004', 'gfanqiang004-0', 'gfanqiang004-1', 'freegoagent465', 'gfanqiang035-8', 'gfanqiang018-9', 'freegoagent896', 'gfanqiang027-8', 'ok126-comeforu-002', 'freegoagent440', 'freegoagent073', 'freegoagent832', 'fghdis9105z-07', 'gfanqiang015-6', 'freegoagent862', 'gfanqiang035-4', 'freegoagent960', 'okp163-comeforu-002', 'freegoagent248', 'ok126-comeforu-006', 'gfanqiang029-2', 'freegoagent058', 'gfanqiang019-3', 'gfanqiang030-4', 'freegoagent629', 'freegoagent706', 'freegoagent718', 'freegoagent774', 'okadm-comeforu-007', 'gfanqiang021-9', 'freegoagent368', 'freegoagent786', 'gfanqiang010-6', 'freegoagent547', 'freegoagent178', 'gfanqiang010-1', 'gfanqiang016-8', 'freegoagent891', 'freegoagent177', 'okadm-comeforu-001', 'freegoagent970', 'freegoagent691', 'gfanqiang036-1', 'gfanqiang018-5', 'freegoagent851', 'gfanqiang015-9', 'freegoagent258', 'freegoagent794', 'freegoagent044', 'gfanqiang036-3', 'freegoagent684', 'x9088-sz-05', 'freegoagent922', 'freegoagent143', 'gfanqiang012-8', 'freegoagent854', 'gfanqiang013-4', 'freegoagent285', 'freegoagent254', 'fghdis9105z-03', 'gfanqiang022-8', 'gfanqiang015-2', 'freegoagent081', 'freegoagent168', 'freegoagent557', 'freegoagent038', 'freegoagent055', 'gfanqiang036-8', 'freegoagent868', 'gfanqiang002-3', 'freegoagent540', 'okp163-comeforu-009', 'qq997-comeforu-004', 'freegoagent106', 'freegoagent030', 'freegoagent338', 'freegoagent654', 'rest126-comeforu-010', 'freegoagent404', 'ok126-comeforu-005', 'gfanqiang021-7', 'freegoagent493', 'freegoagent257', 'freegoagent556', 'gfanqiang026-3', 'freegoagent735', 'gfanqiang022-7', 'freegoagent320', 'freegoagent565', 'freegoagent142', 'freegoagent689', 'freegoagent866', 'gfanqiang036-5', 'gfanqiang033-2', 'freegoagent815', 'gfanqiang024-2', 'okp163-comeforu-007', 'freegoagent301', 'gfanqiang001-8', 'gfanqiang025-9', 'freegoagent160', 'gfanqiang012-9', 'freegoagent154', 'gfanqiang015-5', 'aft126-comeforu-005', 'freegoagent751', 'freegoagent377', 'dboy003163-comeforu-006', 'freegoagent206', 'freegoagent460', 'freegoagent622', 'freegoagent378', 'freegoagent951', 'freegoagent103', 'dboy003163-comeforu-007', 'gfanqiang028-3', 'freegoagent767', 'freegoagent491', 'freegoagent092', 'freegoagent004', 'gfanqiang013-2', 'freegoagent109', 'gfanqiang012-0', 'freegoagent293', 'jk9084s-06', 'freegoagent078', 'gfanqiang033-7', 'freegoagent670', 'freegoagent510', 'gfanqiang020-8', 'freegoagent800', 'freegoagent947', 'freegoagent251', 'freegoagent333', 'gfanqiang008-3', 'freegoagent014', 'freegoagent029', 'freegoagent904', 'freegoagent373', 'gfanqiang030-6', 'freegoagent833', 'freegoagent893', 'freegoagent195', 'freegoagent553', 'freegoagent331', 'freegoagent753', 'freegoagent238', 'freegoagent512', 'freegoagent208', 'freegoagent841', 'freegoagent728', 'freegoagent819', 'freegoagent969', 'freegoagent934', 'gfanqiang033-8', 'freegoagent228', 'freegoagent826', 'freegoagent561', 'fgabootstrap006', 'gfanqiang013-7', 'freegoagent594', 'freegoagent627', 'freegoagent790', 'dboy003163-comeforu-010', 'freegoagent187', 'freegoagent817', 'freegoagent067', 'gfanqiang013-1', 'freegoagent845', 'gfanqiang008-6', 'freegoagent444', 'freegoagent450', 'rest126-comeforu-004', 'aft126-comeforu-002', 'freegoagent850', 'freegoagent280', 'gfanqiang018-7', 'freegoagent902', 'freegoagent544', 'freegoagent593', 'gfanqiang006-3', 'gfanqiang026-9', 'w519163-comeforu-008', 'freegoagent010', 'freegoagent199', 'deepbyeah-comeforu-005', 'gfanqiang019-1', 'freegoagent323', 'dboy003163-comeforu-008', 'freegoagent083', 'freegoagent899', 'freegoagent824', 'freegoagent923', 'gfanqiang035-0', 'gfanqiang008-0', 'freegoagent464', 'freegoagent550', 'freegoagent596', 'pbgl-comeforu-001', 'freegoagent537', 'comeforu-upu2b-010', 'gfanqiang011-5', 'gfanqiang004-2', 'gfanqiang014-7', 'freegoagent723', 'freegoagent101', 'deepb163-comeforu-009', 'freegoagent730', 'freegoagent451', 'freegoagent672', 'gfanqiang012-4', 'freegoagent754', 'gfanqiang027-2', 'freegoagent772', 'freegoagent218', 'freegoagent737', 'freegoagent749', 'gfanqiang003-5', 'comeforu-upu2b-009', 'gfanqiang028-4', 'freegoagent412', 'freegoagent703', 'aft126-comeforu-008', 'gfanqiang026-7', 'freegoagent693', 'freegoagent153', 'freegoagent668', 'freegoagent161', 'freegoagent581', 'gfanqiang004-3', 'dboy003163-comeforu-001', 'gfanqiang004-9', 'freegoagent495', 'freegoagent242', 'freegoagent847', 'freegoagent026', 'qq997-comeforu-002', 'freegoagent917', 'freegoagent785', 'freegoagent339', 'deepbyeah-comeforu-004', 'freegoagent944', 'gfanqiang003-9', 'freegoagent895', 'deepb163-comeforu-004', 'x9088-sz-10', 'gfanqiang018-4', 'freegoagent528', 'freegoagent375', 'freegoagent457', 'freegoagent414', 'freegoagent936', 'freegoagent108', 'gfanqiang034-9', 'freegoagent503', 'freegoagent492', 'freegoagent391', 'x9088-sz-04', 'freegoagent290', 'gfanqiang034-7', 'deepb163-comeforu-003', 'freegoagent647', 'freegoagent468', 'gfanqiang016-5', 'freegoagent888', 'freegoagent618', 'freegoagent395', 'gfanqiang003-4', 'gfanqiang020-9', 'gfanqiang014-3', 'freegoagent269', 'pbgl-comeforu-008', 'gfanqiang012-7', 'freegoagent198', 'gfanqiang012-6', 'freegoagent844', 'freegoagent897', 'gfanqiang009-7', 'x9088-sz-08', 'freegoagent681', 'gfanqiang036-6', 'freegoagent383', 'freegoagent903', 'gfanqiang031-3', 'freegoagent482', 'freegoagent834', 'dboy003163-comeforu-003', 'freegoagent037', 'freegoagent959', 'okp163-comeforu-010', 'gfanqiang034-2', 'gfanqiang022-5', 'gfanqiang007-0', 'freegoagent302', 'fghdis9105z-10', 'gfanqiang030-5', 'freegoagent582', 'freegoagent861', 'gfanqiang035-6', 'freegoagent558', 'freegoagent239', 'gfanqiang035-2', 'szdsdf9104-10', 'fgaupdate006', 'freegoagent773', 'freegoagent589', 'gfanqiang010-5', 'gfanqiang017-2', 'freegoagent643', 'gfanqiang029-4', 'freegoagent661', 'szdsdf9104-02', 'gfanqiang026-8', 'freegoagent709', 'qq997-comeforu-001', 'freegoagent240', 'pbgly-comeforu-002', 'freegoagent266', 'freegoagent499', 'freegoagent442', 'gfanqiang013-6', 'freegoagent764', 'gfanqiang001-3', 'gfanqiang028-2', 'w519163-comeforu-001', 'freegoagent616', 'freegoagent064', 'fgabootstrap003', 'rest126-comeforu-009', 'freegoagent121', 'freegoagent479', 'rest126-comeforu-005', 'freegoagent288', 'freegoagent273', 'freegoagent417', 'freegoagent750', 'freegoagent682', 'freegoagent360', 'freegoagent496', 'freegoagent744', 'gfanqiang000-8', 'freegoagent467', 'gfanqiang031-7', 'freegoagent189', 'freegoagent015', 'gfanqiang019-9', 'freegoagent095', 'freegoagent700', 'freegoagent746', 'freegoagent677', 'freegoagent156', 'freegoagent946', 'freegoagent169', 'gfanqiang025-1', 'freegoagent812', 'deepb163-comeforu-002', 'gfanqiang000-3', 'freegoagent933', 'freegoagent613', 'freegoagent515', 'gfanqiang017-9', 'freegoagent287', 'gfanqiang012-1', 'freegoagent125', 'freegoagent802', 'freegoagent848', 'gfanqiang016-9', 'gfanqiang027-0', 'freegoagent690', 'freegoagent712', 'freegoagent860', 'gfanqiang003-0', 'gfanqiang026-2', 'pbgly-comeforu-005', 'freegoagent347', 'freegoagent699', 'freegoagent796', 'gfanqiang017-4', 'freegoagent929', 'gfanqiang029-6', 'freegoagent343', 'freegoagent521', 'freegoagent172', 'freegoagent500', 'freegoagent427', 'fgg163-comeforu-006', 'freegoagent179', 'freegoagent226', 's-g9085h-03', 'gfanqiang009-8', 'freegoagent429', 'freegoagent948', 'freegoagent466', 'qq997-comeforu-010', 'gfanqiang022-1', 'freegoagent380', 'freegoagent145', 'gfanqiang019-2', 'qq997-comeforu-009', 'gfanqiang018-0', 'jk9084s-05', 'freegoagent546', 'freegoagent663', 'gfanqiang012-2', 'okadm-comeforu-004', 'gfanqiang005-0', 'gfanqiang030-0', 'freegoagent170', 'gfanqiang005-9', 'freegoagent725', 'freegoagent927', 'freegoagent513', 'gfanqiang029-3', 'freegoagent035', 'pbgly-comeforu-001', 'freegoagent328', 'freegoagent140', 'freegoagent694', 'freegoagent838', 'freegoagent679', 'freegoagent075', 'freegoagent938', 'freegoagent454', 'fgaupdate010', 'freegoagent577', 'freegoagent943', 'jk9084s-01', 'gfanqiang034-6', 'gfanqiang003-7', 'freegoagent877', 'ok126-comeforu-004', 'dz126-comeforu-007', 'gfanqiang022-3', 'gfanqiang010-4', 'freegoagent837', 'gfanqiang021-6', 'freegoagent093', 'freegoagent910', 'freegoagent830', 'freegoagent621', 'freegoagent013', 'freegoagent799', 'szdsdf9104-05', 'gfanqiang000-6', 'x9088-sz-09', 'freegoagent362', 'freegoagent349', 'freegoagent680', 'freegoagent659', 'freegoagent486', 'freegoagent405', 'freegoagent805', 'freegoagent023', 'freegoagent274', 'freegoagent407', 'gfanqiang010-9', 'gfanqiang029-9', 'freegoagent525', 'qq997-comeforu-008', 'freegoagent079', 'freegoagent950', 'freegoagent531', 'freegoagent930', 'freegoagent184', 'gfanqiang014-6', 'qq997-comeforu-003', 'freegoagent059', 'gfanqiang018-3', 'freegoagent698', 'freegoagent963', 'fghdis9105z-02', 'freegoagent644', 'gfanqiang009-2', 'freegoagent371', 'freegoagent162', 'gfanqiang026-4', 'freegoagent584', 'freegoagent520', 'gfanqiang016-0', 'gfanqiang004-6', 'freegoagent894', 'gfanqiang016-3', 'freegoagent418', 'freegoagent843', 'freegoagent506', 'freegoagent146', 'freegoagent275', 'gfanqiang036-2', 'dz126-comeforu-009', 'qq997-comeforu-004', 'freegoagent325', 'okadm-comeforu-010', 'freegoagent192', 'freegoagent600', 'freegoagent286', 'gfanqiang013-0', 'gfanqiang002-6', 'fgabootstrap010', 'gfanqiang029-0', 'freegoagent678', 'freegoagent928', 'freegoagent748', 'freegoagent900', 'freegoagent424', 'freegoagent317', 'freegoagent878', 'gfanqiang000-7', 'jk9084s-02', 's-g9085h-10', 'freegoagent859', 'freegoagent458', 'freegoagent214', 'freegoagent053', 'freegoagent003', 'freegoagent610', 'dz126-comeforu-010', 'okp163-comeforu-008', 'freegoagent425', 'fgabootstrap001', 'freegoagent128', 'gfanqiang008-1', 'freegoagent818', 'gfanqiang035-9', 'gfanqiang006-8', 'gfanqiang017-0', 'freegoagent330', 'freegoagent176', 'aft126-comeforu-006', 'gfanqiang023-4', 'pbgly-comeforu-004', 'freegoagent420', 'freegoagent408', 'freegoagent731', 's-g9085h-08', 's-g9085h-07', 'gfanqiang031-0', 'okp163-comeforu-003', 'freegoagent321', 'freegoagent858', 'freegoagent342', 'freegoagent278', 'w519163-comeforu-003', 'gfanqiang010-7', 'gfanqiang014-9', 'freegoagent031', 'qq997-comeforu-007', 'freegoagent080', 'freegoagent953', 'gfanqiang025-7', 'freegoagent554', 'gfanqiang017-7', 'gfanqiang023-5', 'freegoagent032', 'freegoagent778', 'freegoagent650', 'freegoagent798', 'gfanqiang019-0', 'freegoagent225', 'freegoagent939', 'freegoagent811', 'freegoagent640', 'comeforu-upu2b-002', 'freegoagent586', 'freegoagent384', 'deepb163-comeforu-007', 'freegoagent686', 'gfanqiang014-5', 'freegoagent605', 'freegoagent357', 'freegoagent394', 'freegoagent441', 'pbgl-comeforu-010', 'freegoagent726', 'gfanqiang028-5', 'freegoagent337', 'szdsdf9104-03', 'freegoagent788', 'freegoagent183', 'freegoagent732', 'freegoagent595', 'freegoagent277', 'freegoagent382', 'freegoagent071', 'freegoagent736', 'freegoagent403', 'freegoagent433', 'freegoagent519', 'freegoagent074', 'freegoagent734', 'freegoagent955', 'freegoagent526', 'gfanqiang022-0', 'freegoagent294', 'freegoagent102', 'freegoagent105', 'freegoagent185', 'gfanqiang004-8', 'freegoagent019', 'fgabootstrap009', 'gfanqiang033-1', 'gfanqiang022-2', 'gfanqiang000-5', 'freegoagent041', 'freegoagent007', 'freegoagent099', 'freegoagent502', 'deepb163-comeforu-005', 'freegoagent685', 'deepbyeah-comeforu-001', 'freegoagent443', 'szdsdf9104-04', 'gfanqiang010-8', 'freegoagent359', 'rest126-comeforu-003', 'freegoagent527', 'freegoagent129', 'jk9084s-10', 'gfanqiang003-6', 'gfanqiang024-1', 'freegoagent086', 'freegoagent296', 'comeforu-upu2b-003', 'freegoagent765', 'freegoagent542', 'freegoagent623', 'freegoagent474', 'gfanqiang023-2', 'ok126-comeforu-008', 'freegoagent497', 'freegoagent138', 'freegoagent247', 'w519163-comeforu-002', 'gfanqiang004-5', 'aft126-comeforu-007', 'freegoagent669', 'freegoagent733', 'freegoagent473', 'freegoagent810', 'freegoagent171', 'freegoagent421', 'gfanqiang005-3', 'gfanqiang006-0', 'fgabootstrap005', 'freegoagent755', 'freegoagent042', 'gfanqiang030-3', 'dz126-comeforu-004', 'gfanqiang020-1', 'gfanqiang031-4', 'gfanqiang008-2', 'freegoagent141', 's-g9085h-05', 'okadm-comeforu-002', 'gfanqiang016-6', 'freegoagent628', 'dboy003163-comeforu-009', 'gfanqiang034-3', 'freegoagent551', 'x9088-sz-07', 'gfanqiang005-5', 'freegoagent369', 'freegoagent602', 'freegoagent538', 'gfanqiang020-0', 'freegoagent448', 'freegoagent456', 'freegoagent159', 'freegoagent543', 'gfanqiang022-6', 'freegoagent131', 'fgaupdate005', 'gfanqiang011-4', 'gfanqiang032-6', 'freegoagent165', 'freegoagent762', 'gfanqiang031-2', 'gfanqiang028-0', 'gfanqiang024-6', 'freegoagent671', 'gfanqiang000-4', 'freegoagent566', 'freegoagent008', 'gfanqiang030-1', 'gfanqiang025-5', 'freegoagent259', 'freegoagent005', 'gfanqiang026-1', 'gfanqiang015-1', 'freegoagent423', 'gfanqiang009-5', 'freegoagent501', 'ok126-comeforu-009', 'freegoagent574', 'freegoagent431', 'gfanqiang002-5', 'fgg163-comeforu-003', 'freegoagent675', 'freegoagent352', 'freegoagent048', 'freegoagent049', 'freegoagent136', 'freegoagent098', 'gfanqiang005-4', 'freegoagent406', 'freegoagent387', 'freegoagent615', 'freegoagent282', 'freegoagent857', 'freegoagent649', 'freegoagent025', 'freegoagent881', 'freegoagent475', 'gfanqiang027-7', 'freegoagent702', 'gfanqiang028-8', 'freegoagent319', 'freegoagent823', 'freegoagent216', 'freegoagent836', 'freegoagent687', 'dz126-comeforu-006', 'freegoagent701', 'freegoagent791', 'gfanqiang018-2', 'pbgly-comeforu-010', 'fgg163-comeforu-004', 'freegoagent632', 'fghdis9105z-05', 'freegoagent110', 'freegoagent082', 'freegoagent033', 'freegoagent720', 'freegoagent504', 'jk9084s-09', 'freegoagent463', 'jk9084s-07', 'freegoagent097', 'freegoagent865', 'comeforu-upu2b-007', 'gfanqiang026-0', 'comeforu-upu2b-005', 'gfanqiang002-1', 'freegoagent193', 'freegoagent912', 'freegoagent415', 'freegoagent350', 'freegoagent472', 'gfanqiang005-8', 'dz126-comeforu-003', 'comeforu-upu2b-001', 'freegoagent181', 'szdsdf9104-07', 'gfanqiang009-0', 'freegoagent283', 'gfanqiang025-0', 'deepb163-comeforu-010', 'freegoagent346', 'freegoagent072', 'freegoagent863', 'freegoagent562', 'freegoagent265', 'freegoagent149', 'freegoagent592', 'freegoagent530', 'freegoagent210', 'freegoagent611', 'gfanqiang000-2', 'freegoagent002', 'gfanqiang017-8', 's-g9085h-09', 'gfanqiang021-2', 'freegoagent879', 'gfanqiang032-3', 'freegoagent310', 'freegoagent651', 'freegoagent249', 'qq997-comeforu-006', 'freegoagent484', 'freegoagent925', 'freegoagent390', 'freegoagent518', 'gfanqiang025-3', 'freegoagent601', 'freegoagent236', 'gfanqiang007-6', 'freegoagent453', 'gfanqiang011-2', 'gfanqiang015-0', 'freegoagent716', 'gfanqiang027-1', 'gfanqiang032-7', 'gfanqiang016-4', 'freegoagent351', 'freegoagent882', 'gfanqiang006-1', 'deepbyeah-comeforu-010', 'gfanqiang014-1', 'freegoagent017', 'freegoagent426', 'freegoagent756', 'gfanqiang011-0', 'freegoagent831', 'freegoagent481', 'freegoagent237', 'freegoagent814', 'okp163-comeforu-005', 'freegoagent911', 'freegoagent221', 'mhyeah-comeforu-007', 'gfanqiang024-5', 'freegoagent284', 'freegoagent130', 'freegoagent147', 'freegoagent163', 'fgaupdate009', 'freegoagent077', 'freegoagent822', 'freegoagent890', 'gfanqiang020-4', 'okadm-comeforu-006', 'freegoagent402', 'freegoagent152', 'gfanqiang021-4', 'gfanqiang013-8', 'freegoagent036', 'freegoagent842', 'freegoagent909', 'freegoagent409', 'freegoagent298', 'freegoagent635', 'freegoagent914', 'pbgl-comeforu-005', 'fgabootstrap004', 'gfanqiang010-2', 'freegoagent447', 'gfanqiang017-3', 'szdsdf9104-06', 'freegoagent932', 'freegoagent022', 'gfanqiang004-4', 'qq997-comeforu-007', 'fghdis9105z-08', 'freegoagent855', 'freegoagent370', 'gfanqiang006-9', 'gfanqiang011-7', 'gfanqiang011-9', 'freegoagent856', 'freegoagent411', 'gfanqiang025-8', 'fgaupdate003', 'freegoagent260', 'pbgl-comeforu-002', 'w519163-comeforu-005', 'freegoagent619', 'gfanqiang025-4', 'freegoagent642', 'freegoagent246', 'freegoagent096', 'szdsdf9104-09', 'fghdis9105z-01', 'freegoagent585', 'gfanqiang032-2', 'freegoagent436', 'freegoagent386', 'freegoagent704', 'freegoagent548', 'gfanqiang002-4', 'freegoagent021', 'freegoagent272', 'freegoagent462', 'freegoagent419', 'freegoagent827', 'pbgl-comeforu-003', 'freegoagent186', 'gfanqiang002-7', 'freegoagent625', 'gfanqiang016-1', 'freegoagent534', 'mhyeah-comeforu-001', 'comeforu-upu2b-006', 'freegoagent967', 'freegoagent587', 'freegoagent529', 'freegoagent062', 'gfanqiang009-9', 'freegoagent416', 'qq997-comeforu-001', 'freegoagent212', 'freegoagent617', 'pbgly-comeforu-009', 'freegoagent569', 'freegoagent792', 'freegoagent958', 'freegoagent784', 'freegoagent367', 'freegoagent494', 'freegoagent892', 'freegoagent400', 'freegoagent410', 'freegoagent150', 'freegoagent469', 'gfanqiang019-8', 'freegoagent345', 'freegoagent393', 'freegoagent219', 'gfanqiang011-1', 'deepb163-comeforu-006', 'okadm-comeforu-009', 'freegoagent267', 'freegoagent445', 's-g9085h-01', 'freegoagent011', 'freegoagent364', 'freegoagent715', 'freegoagent722', 'freegoagent046', 'gfanqiang003-3', 'gfanqiang033-4', 'gfanqiang032-1', 'gfanqiang027-3', 'freegoagent366', 'freegoagent094', 'freegoagent779', 'fganr002', 'freegoagent063', 'fgg163-comeforu-002', 'freegoagent771', 'freegoagent887', 'freegoagent821', 'freegoagent949', 'freegoagent034', 'freegoagent692', 'gfanqiang007-1', 'dz126-comeforu-002', 'gfanqiang031-9', 'gfanqiang027-9', 'freegoagent372', 'gfanqiang035-1', 'gfanqiang028-6', 'freegoagent470', 'gfanqiang013-3', 'freegoagent066', 'freegoagent509', 'freegoagent797', 'freegoagent174', 'freegoagent167', 'gfanqiang023-8', 'freegoagent076', 'freegoagent223', 'gfanqiang016-7', 'freegoagent255', 'freegoagent202', 'fgaupdate002', 'freegoagent770', 'w519163-comeforu-009', 'qq997-comeforu-005', 'gfanqiang031-8', 'fgg163-comeforu-001', 'gfanqiang021-5', 'freegoagent264', 'freegoagent324', 'gfanqiang027-5', 'freegoagent289', 'freegoagent507', 'freegoagent511', 'freegoagent884', 'jk9084s-04', 'freegoagent305', 'gfanqiang009-4', 'freegoagent688', 'gfanqiang002-0', 'gfanqiang023-1', 'freegoagent104', 'freegoagent871', 'gfanqiang023-6', 'freegoagent919', 'freegoagent244', 'qq997-comeforu-002', 'okadm-comeforu-008', 'gfanqiang014-0', 'freegoagent570', 'freegoagent880', 'freegoagent027', 'freegoagent614', 'freegoagent182', 'gfanqiang001-1', 'dboy003163-comeforu-002', 'gfanqiang001-0', 'freegoagent040', 'freegoagent439', 'freegoagent780', 'freegoagent580', 'freegoagent579', 'freegoagent852', 'freegoagent657', 'fgabootstrap007', 'freegoagent356', 'freegoagent652', 'freegoagent608', 'freegoagent054', 'freegoagent085', 'freegoagent180', 'freegoagent279', 'aft126-comeforu-009', 'freegoagent166', 'freegoagent045', 'aft126-comeforu-010', 'freegoagent766', 'freegoagent200', 'freegoagent133', 'gfanqiang015-3', 'freegoagent915', 'gfanqiang036-4', 'freegoagent883', 'gfanqiang006-2', 'freegoagent446', 'freegoagent559', 'freegoagent886', 'freegoagent636', 'freegoagent194', 'freegoagent532', 'w519163-comeforu-004', 'freegoagent954', 'deepbyeah-comeforu-006', 'freegoagent801', 'freegoagent835', 'gfanqiang006-6', 'gfanqiang030-7', 'freegoagent721', 'freegoagent295', 'freegoagent964', 'fgabootstrap008', 'freegoagent664', 'gfanqiang003-8', 'gfanqiang025-6', 'freegoagent311', 'ok126-comeforu-010', 'gfanqiang007-5', 'freegoagent759', 'freegoagent304', 'mhyeah-comeforu-003', 'freegoagent804', 'freegoagent885', 'freegoagent876', 'pbgl-comeforu-004', 'freegoagent781', 'freegoagent724', 'freegoagent913', 'rest126-comeforu-006', 'freegoagent612', 'freegoagent144', 'freegoagent787', 'dz126-comeforu-005', 'freegoagent598', 'mhyeah-comeforu-009', 'freegoagent768', 'freegoagent743', 'gfanqiang011-6', 'freegoagent197', 'fganr001', 'freegoagent203', 'freegoagent665', 'freegoagent758', 'freegoagent901', 'ok126-comeforu-003', 'w519163-comeforu-010', 'freegoagent747', 'freegoagent874', 'freegoagent299', 'fgaupdate008', 'gfanqiang006-4', 'freegoagent009', 'freegoagent340', 'freegoagent354', 'freegoagent956', 'pbgl-comeforu-007', 'freegoagent385', 'okadm-comeforu-005', 'freegoagent599', 'freegoagent052', 'freegoagent209', 'gfanqiang032-9', 'freegoagent229', 'freegoagent012', 'gfanqiang015-8', 'gfanqiang036-7', 'freegoagent047', 'gfanqiang017-5', 'freegoagent232', 'freegoagent539', 'freegoagent603', 'freegoagent312', 'freegoagent820', 'freegoagent215', 'gfanqiang033-0', 'freegoagent020', 'freegoagent962', 'gfanqiang001-7', 'gfanqiang008-7', 'freegoagent327', 'gfanqiang032-5', 'freegoagent271', 'freegoagent828', 'freegoagent639', 'gfanqiang034-4', 'freegoagent571', 'pbgl-comeforu-009', 'gfanqiang000-1', 'fgg163-comeforu-005', 'gfanqiang029-5', 'gfanqiang033-6', 'freegoagent535', 'freegoagent906', 'freegoagent560', 'fgg163-comeforu-009', 'freegoagent213', 'freegoagent782', 'freegoagent422', 'freegoagent609', 'freegoagent329', 'freegoagent217', 'gfanqiang001-5', 'gfanqiang024-7', 'gfanqiang030-9', 'freegoagent241', 'freegoagent122', 'freegoagent760', 'gfanqiang019-6', 'gfanqiang030-8', 'freegoagent250', 'pbgl-comeforu-006', 'gfanqiang007-3', 'gfanqiang011-8', 'freegoagent151', 'freegoagent738', 'gfanqiang032-4', 'freegoagent807', 'mhyeah-comeforu-002', 'freegoagent555', 'freegoagent875', 'freegoagent646', 'freegoagent353', 'freegoagent455', 'fgaupdate004', 'gfanqiang028-9', 'gfanqiang017-6', 'dz126-comeforu-008', 'gfanqiang024-9', 'gfanqiang036-0', 'qq997-comeforu-006', 'freegoagent050', 'freegoagent907', 'freegoagent039', 'freegoagent392', 'freegoagent920', 'freegoagent508', 'gfanqiang024-8', 'freegoagent809', 'gfanqiang030-2', 'gfanqiang003-1', 's-g9085h-04', 'qq997-comeforu-005', 'freegoagent656', 'freegoagent846', 'qq997-comeforu-009', 'freegoagent477', 'freegoagent173', 'freegoagent434', 'freegoagent789', 'freegoagent315', 'gfanqiang028-7', 'gfanqiang029-8', 'freegoagent230', 'freegoagent158', 'dboy003163-comeforu-004', 'gfanqiang022-9', 'freegoagent667', 'freegoagent840', 'freegoagent483', 'w519163-comeforu-006', 'fgaupdate007', 'freegoagent660', 'gfanqiang009-1', 'freegoagent829', 'gfanqiang006-5', 'freegoagent313', 'gfanqiang021-3', 'rest126-comeforu-008', 'gfanqiang034-1', 'freegoagent864', 'gfanqiang035-3', 'gfanqiang029-1', 'freegoagent607', 'freegoagent307', 'szdsdf9104-08', 'gfanqiang035-7', 'freegoagent683', 'deepbyeah-comeforu-009', 'freegoagent480', 'freegoagent662', 'freegoagent024', 'freegoagent065', 'freegoagent697', 'freegoagent326', 'freegoagent090', 'freegoagent243', 'mhyeah-comeforu-008', 'gfanqiang033-3', 'gfanqiang031-1', 'gfanqiang021-8', 'freegoagent263', 'freegoagent070', 'aft126-comeforu-003', 'gfanqiang008-9', 'szdsdf9104-01', 'gfanqiang010-0', 'freegoagent488', 'pbgly-comeforu-008', 'deepbyeah-comeforu-002', 'freegoagent573', 'comeforu-upu2b-004', 'freegoagent292', 'freegoagent398', 'jk9084s-08', 'fghdis9105z-04', 'freegoagent399', 'freegoagent869', 'gfanqiang020-7', 'okp163-comeforu-004', 'freegoagent089', 'pbgly-comeforu-003', 'freegoagent471', 'freegoagent740', 'aft126-comeforu-001', 'freegoagent155', 'gfanqiang001-2', 'freegoagent381', 'freegoagent637', 'freegoagent965', 'freegoagent921', 'gfanqiang022-4', 'freegoagent695', 'freegoagent552', 'freegoagent061', 'freegoagent438', 'gfanqiang023-3', 'freegoagent739', 'gfanqiang001-9', 'freegoagent126', 'freegoagent245', 'fgaupdate001', 'gfanqiang019-7', 'freegoagent234', 'freegoagent087', 'gfanqiang013-9', 'deepbyeah-comeforu-007', 'freegoagent107', 'freegoagent591', 'freegoagent207', 'freegoagent043', 'gfanqiang000-0', 'pbgly-comeforu-006', 'freegoagent942', 'freegoagent638', 'gfanqiang014-8', 'dboy003163-comeforu-005', 'freegoagent710', 'freegoagent291', 'freegoagent124', 'freegoagent449', 'freegoagent148', 'deepb163-comeforu-008', 'freegoagent803', 'freegoagent322', 'gfanqiang010-3', 'freegoagent564', 'gfanqiang011-3', 'gfanqiang008-5', 'gfanqiang008-4', 'gfanqiang007-4', 'freegoagent318', 'freegoagent222', 'freegoagent776', 'x9088-sz-03', 'freegoagent655', 'freegoagent783', 'freegoagent626', 'freegoagent069', 'freegoagent485', 'fgg163-comeforu-008', 'freegoagent583', 'freegoagent205', 'freegoagent825', 'freegoagent127', 'freegoagent708', 'freegoagent134', 'gfanqiang009-3', 'freegoagent432', 'freegoagent498', 'gfanqiang009-6', 'mhyeah-comeforu-006', 'freegoagent536', 'gfanqiang015-7', 'gfanqiang002-8', 'freegoagent132', 'gfanqiang021-0', 'freegoagent374', 'gfanqiang020-6', 'freegoagent437', 'gfanqiang002-2', 'freegoagent533', 'freegoagent478', 'freegoagent227', 'freegoagent729', 'freegoagent898', 'gfanqiang018-1', 'freegoagent428', 'freegoagent001', 'freegoagent763', 'gfanqiang032-0', 'freegoagent461', 'freegoagent624', 'freegoagent276', 'freegoagent256', 'gfanqiang032-8', 'freegoagent348', 'gfanqiang018-8', 'freegoagent523', 'gfanqiang031-5', 'freegoagent388', 'freegoagent303', 'freegoagent517', 'freegoagent413', 'gfanqiang025-2', 'gfanqiang014-4', 'gfanqiang005-7', 'gfanqiang026-6', 'freegoagent341', 'freegoagent270', 'gfanqiang000-9', 'freegoagent867', 'gfanqiang001-4', 'freegoagent188', 'freegoagent926', 'gfanqiang002-9', 'freegoagent795', 'freegoagent645', 'pbgly-comeforu-007', 'freegoagent332', 'freegoagent705', 'freegoagent336', 'freegoagent968', 'gfanqiang033-9', 'gfanqiang001-6', 'freegoagent966', 'freegoagent157', 'gfanqiang018-6', 'freegoagent757', 's-g9085h-02', 'freegoagent676', 'qq997-comeforu-008', 'freegoagent666', 'freegoagent924', 'freegoagent396', 'qq997-comeforu-010', 'gfanqiang012-3', 'freegoagent872', 'freegoagent713', 'freegoagent634', 'freegoagent300', 'freegoagent590', 'freegoagent849', 'x9088-sz-02', 'freegoagent235', 'freegoagent262', 'x9088-sz-06', 'freegoagent233', 'gfanqiang029-7', 'freegoagent334', 'freegoagent459', 'gfanqiang023-0', 'gfanqiang021-1', 'freegoagent231', 'freegoagent714', 'gfanqiang034-8', 'gfanqiang012-5', 'freegoagent727', 'gfanqiang027-4', 'fgg163-comeforu-010', 'gfanqiang007-9', 'jk9084s-03', 'gfanqiang024-3', 'freegoagent745', 'freegoagent945', 'freegoagent658', 'gfanqiang023-9', 'freegoagent620', 'freegoagent522', 'fghdis9105z-09', 'freegoagent489', 'freegoagent563', 'mhyeah-comeforu-010', 'freegoagent196', 'freegoagent524', 'freegoagent314', 'freegoagent576', 'freegoagent028', 'gfanqiang027-6'], listen='8087', password='wwqgtxx-wallproxy2.1-0.10', path='/fetch.py', scheme='https', hosts=google_hosts, max_threads=3, fetch_mode=1)

    PacFile, RuleList, HostList = import_from('pac')
    forcehttps_sites = RuleList('http://*.appspot.com/ \n http://*.google.com/ \n http://*.google.com.hk/ \n http://*.googlecode.com/ \n http://*.googleusercontent.com/ \n http://*.blogger.com/ \n @@http://books.google.com/ \n @@http://translate.google.com/ \n @@http://scholar.google.com/ \n @@http://feedproxy.google.com/ \n @@http://fusion.google.com/ \n @@http://picasa.google.com/ \n @@http://*pack.google.com/ \n @@http://*android.clients.google.com/ \n @@http://wenda.google.com.hk/ \n @@http://www.google.com*/imgres? \n @@http://www.google.com*/translate_t? \n @@http://www.google.com/analytics/ \n @@http://wiki.*.googlecode.com/ \n @@http:/// \n @@http://website.*.googlecode.com/ \n @@http://www.google.com*/custom? \n @@http://www.google.com/dl/')
    autorange_rules = RuleList('||c.youtube.com \n ||c.docs.google.com \n ||googlevideo.com \n http*://av.vimeo.com/ \n http*://smile-*.nicovideo.jp/ \n http*://video.*.fbcdn.net/ \n http*://s*.last.fm/ \n http*://x*.last.fm/ \n /^https?:\\/\\/[^\\/]+\\/[^?]+\\.(?:f4v|flv|hlv|m4v|mp4|mp3|ogg|avi|exe)(?:$|\\?)/ \n http*://*.googleusercontent.com/videoplayback?')
    _GAE = GAE; GAE = lambda req: _GAE(req, autorange_rules.match(req.url, req.proxy_host[0]))
    import re; useragent_match = re.compile('(?i)mobile').search
    useragent_rules = RuleList('||twitter.com')
    withgae_sites = RuleList('||c.docs.google.com \n ||translate.google.com \n http*://books.google.com/books?id= \n http*://*.googleusercontent.com/videoplayback?')
    notruehttps_sites = HostList('.docs.google.com translate.google.com books.google.com')
    truehttps_sites = HostList('.appspot.com .google.com .google.com.hk .googlecode.com .googleusercontent.com .googlegroups.com .google-analytics.com .gstatic.com .googleapis.com .blogger.com .ggpht.com .facebook.com')
    crlf_rules = RuleList('/^https?:\\/\\/[^\\/]+\\.c\\.youtube\\.com\\/liveplay\\?/ \n /^https?:\\/\\/upload\\.youtube\\.com\\// \n /^https?:\\/\\/www\\.youtube\\.com\\/upload\\//')
    hosts_rules = RuleList(' \n ||appspot.com \n ||google.com \n ||google.com.hk \n ||googlecode.com \n ||googleusercontent.com \n ||googlegroups.com \n ||google-analytics.com \n ||gstatic.com \n ||googleapis.com \n ||blogger.com \n ||ggpht.com')
    _HttpsFallback = (GAE,)
    nofallback_rules = RuleList('/^https?:\\/\\/(?:[\\w-]+|127(?:\\.\\d+){3}|10(?:\\.\\d+){3}|192\\.168(?:\\.\\d+){2}|172\\.[1-3]\\d(?:\\.\\d+){2}|\\[.+?\\])(?::\\d+)?\\//')
    def FORWARD(req):
        if req.proxy_type.endswith('http'):
            if nofallback_rules.match(req.url, req.proxy_host[0]):
                return RAW_FORWARD(req)
            return RAW_FORWARD(req, GAE)
        url = build_fake_url(req.proxy_type, req.proxy_host)
        if nofallback_rules.match(url, req.proxy_host[0]):
            return RAW_FORWARD(req)
        return RAW_FORWARD(req, _HttpsFallback)

    rulelist = (
        (RuleList(['https://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt', 'userlist.ini']), GAE),
    )
    httpslist = (
        (rulelist[0][0], None),
    )
    unparse_netloc = import_from('utils')
    def build_fake_url(type, host):
        if type == 'https': port = 443
        elif host[1] % 1000 == 443: type, port = 'https', 443
        else: type, port = 'http', 80
        return '%s://%s/' % (type, unparse_netloc(host, port))

    def find_gae_handler(req):
        proxy_type = req.proxy_type
        host, port = req.proxy_host
        if proxy_type.endswith('http'):
            url = req.url
            if useragent_match(req.headers.get('User-Agent','')) and useragent_rules.match(url, host):
                req.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4'
            if withgae_sites.match(url, host):
                return GAE
            needhttps = req.scheme == 'http' and forcehttps_sites.match(url, host) and req.content_length == 0
            if needhttps and getattr(req, '_r', '') != url:
                req._r = url
                return redirect_https
            if crlf_rules.match(url, host):
                req.crlf = 1
                return FORWARD
            if not needhttps and hosts_rules.match(url, host):
                return FORWARD
            return GAE
        if notruehttps_sites.match(host): return
        if truehttps_sites.match(host): return FORWARD
    paas.data['GAE_server'].find_handler = find_gae_handler

    def find_proxy_handler(req):
        proxy_type = req.proxy_type
        host, port = req.proxy_host
        if proxy_type.endswith('http'):
            url = req.url
            if useragent_match(req.headers.get('User-Agent','')) and useragent_rules.match(url, host):
                req.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4'
            if withgae_sites.match(url, host):
                return GAE
            needhttps = req.scheme == 'http' and forcehttps_sites.match(url, host) and req.content_length == 0
            if needhttps and getattr(req, '_r', '') != url:
                req._r = url
                return redirect_https
            if crlf_rules.match(url, host):
                req.crlf = 1
                return FORWARD
            if not needhttps and hosts_rules.match(url, host):
                return FORWARD
            for rule,target in rulelist:
                if rule.match(url, host):
                    return target
            return FORWARD
        if notruehttps_sites.match(host): return
        if truehttps_sites.match(host): return FORWARD
        url = build_fake_url(proxy_type, (host, port))
        for rule,target in httpslist:
            if rule.match(url, host):
                return target
        return FORWARD
    return find_proxy_handler