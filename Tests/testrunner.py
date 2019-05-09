from Tests.login import login
import unittest,os,HtmlTestRunner

login_tests=unittest.TestLoader().loadTestsFromTestCase(login)
smoke_tests=unittest.TestSuite([login_tests])
#testRunner = HtmlTestRunner.HTMLTestRunner(output='D:/Personal'))

dir = os.getcwd()
outfile = open(dir + '\SmokeTestReport.html', 'w')
runner = HtmlTestRunner.HTMLTestRunner(stream=outfile)
runner.run(smoke_tests)
