from pathlib import Path
p=Path(__file__).parent
base=(p/'src/legacy-app.js').read_text()
base=base.replace("'vbna.chapter11.vn'", "'vbnachapter11.com'")
base=base.replace("value=\"07:00\"", "value=\"13:30\"")
base=base.replace("location.href=params.get('next')||homeForUser(u)", "location.href=homeForUser(u)")
base=base.replace("let S=load();", "let S=load();")
base=base[:base.index('/* init */')]
parts=['core','public','reports','operations','finance','settings','integration','vbna-directory','member-import','prestige','approved-design','vbna-verbatim','catalog','v7','overview-v7','footer-sync-v7','login-v7','role-matrix-v7','dashboard-v7','member-assignment-v7','finance-fix-v7','reset-v7','luxury-v7','department-tools-v7','guest-intake-v7','post-actions-v7','training-actions-v7','report-layout-v7','access-meetings-v7','unified-admin-v7','mobile-app-v7']
base+='\n'.join((p/f'src/{f}.js').read_text() for f in parts)
base+='\ndocument.addEventListener(\'DOMContentLoaded\',bootV6);\n})();\n'
(p/'app.js').write_text((p/'src/v7-rules.js').read_text()+'\n'+(p/'src/dashboard-rules-v7.js').read_text()+'\n'+(p/'src/finance-rules-v7.js').read_text()+'\n'+(p/'src/reset-rules-v7.js').read_text()+'\n'+base)
for f in p.glob('*.html'):
 s=f.read_text().replace('vbna.chapter11.vn','vbnachapter11.com')
 s=s.replace('<script defer src="app.js"></script>', '<script defer src="vendor/jszip.min.js"></script><script defer src="vendor/qrcode.js"></script><script defer src="app.js"></script>') if 'vendor/jszip' not in s else s
 if 'v6.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="v6.css"></head>')
 if 'v7.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="v7.css"></head>')
 if 'overview-v7.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="overview-v7.css"></head>')
 if 'footer-v7.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="footer-v7.css"></head>')
 s=s.replace('vbna.chapter11.com','vbnachapter11.com')
 if 'login-v7.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="login-v7.css"></head>')
 if 'role-matrix-v7.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="role-matrix-v7.css"></head>')
 if 'dashboard-v7.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="dashboard-v7.css"></head>')
 if 'luxury-v7.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="luxury-v7.css"></head>')
 if f.name=='admin.html' and 'mobile-app-v7.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="mobile-app-v7.css"></head>')
 f.write_text(s)
