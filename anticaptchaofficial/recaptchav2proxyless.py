from antinetworking import *
import time


class recaptchaV2Proxyless(antiNetworking):

    def solve_and_return_solution(self):
        if self.create_task({
            "clientKey": self.client_key,
            "task": {
                "type": "NoCaptchaTaskProxyless",
                "websiteURL": self.website_url,
                "websiteKey": self.website_key,
                "websiteSToken": self.website_stoken
            }
        }) == 1:
            self.log("created task with id "+str(self.task_id))
        else:
            self.log("could not create task")
            self.log(self.err_string)
            return 0
        #checking result
        time.sleep(3)
        task_result = self.wait_for_result(300)
        if task_result == 0:
            return 0
        else:
            return task_result["solution"]["gRecaptchaResponse"]
