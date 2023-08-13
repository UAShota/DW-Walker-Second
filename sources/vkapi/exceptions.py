# -*- coding: utf-8 -*-
"""
:authors: python273
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2019 python273
"""


TWOFACTOR_CODE = -2
HTTP_ERROR_CODE = -1
TOO_MANY_RPS_CODE = 6
CAPTCHA_ERROR_CODE = 14
NEED_VALIDATION_CODE = 17


class VkApiError(Exception):
    """ Api error """
    pass


class AccessDenied(VkApiError):
    """ Access denied """
    pass


class AuthError(VkApiError):
    """ Auth error """
    pass


class LoginRequired(AuthError):
    """ Login required """
    pass


class PasswordRequired(AuthError):
    """ Password required """
    pass


class BadPassword(AuthError):
    """ Bad password """
    pass


class AccountBlocked(AuthError):
    """ Account blocked """
    pass


class TwoFactorError(AuthError):
    """ Two factor auth error """
    pass


class SecurityCheck(AuthError):
    """ Check user security """

    def __init__(self, phone_prefix=None, phone_postfix=None, response=None):
        super(SecurityCheck, self).__init__()

        self.phone_prefix = phone_prefix
        self.phone_postfix = phone_postfix
        self.response = response

    def __str__(self):
        if self.phone_prefix and self.phone_postfix:
            return 'Security check. Enter number: {} ... {}'.format(
                self.phone_prefix, self.phone_postfix
            )
        else:
            return ('Security check. Phone prefix and postfix are not detected.'
                    ' Please send bugreport (response in self.response)')


class ApiError(VkApiError):
    """ Analyze api error """

    def __init__(self, vk, method, values, raw, error):
        super(ApiError, self).__init__()

        self.vk = vk
        self.method = method
        self.values = values
        self.raw = raw
        self.code = error['error_code']
        self.error = error

    def try_method(self):
        """ Отправить запрос заново """

        return self.vk.method(self.method, self.values, raw=self.raw)

    def __str__(self):
        return '[{}] {}'.format(self.error['error_code'],
                                self.error['error_msg'])


class ApiHttpError(VkApiError):
    """ Analyze http error """

    def __init__(self, vk, method, values, raw, response):
        super(ApiHttpError, self).__init__()

        self.vk = vk
        self.method = method
        self.values = values
        self.raw = raw
        self.response = response

    def try_method(self):
        """ Отправить запрос заново """

        return self.vk.method(self.method, self.values, raw=self.raw)

    def __str__(self):
        return 'Response code {}'.format(self.response.status_code)


class Captcha(VkApiError):
    """ Captcha validator """

    def __init__(self, vk, captcha_sid, func, args=None, kwargs=None, url=None):
        super(Captcha, self).__init__()

        self.vk = vk
        self.sid = captcha_sid
        self.func = func
        self.args = args or ()
        self.kwargs = kwargs or {}

        self.code = CAPTCHA_ERROR_CODE

        self.key = None
        self.url = url
        self.image = None

    def get_url(self):
        """ Получить ссылку на изображение капчи """

        if not self.url:
            self.url = 'https://api.vk.com/captcha.php?sid={}'.format(self.sid)

        return self.url

    def get_image(self):
        """ Получить изображение капчи (jpg) """

        if not self.image:
            self.image = self.vk.http.get(self.get_url()).content

        return self.image

    def try_again(self, key=None):
        """ Отправить запрос заново с ответом капчи

        :param key: ответ капчи
        """

        if key:
            self.key = key

            self.kwargs.update({
                'captcha_sid': self.sid,
                'captcha_key': self.key
            })

        return self.func(*self.args, **self.kwargs)

    def __str__(self):
        return 'Captcha needed'


class VkAudioException(Exception):
    """ Audio exception """
    pass


class VkAudioUrlDecodeError(VkAudioException):
    """ Audio error """
    pass


class VkToolsException(VkApiError):
    """ Tool exception """
    def __init__(self, *args, response=None):
        super().__init__(*args)
        self.response = response


class VkRequestsPoolException(Exception):
    """ Pool exception """
    def __init__(self, error, *args):
        self.error = error
        super(VkRequestsPoolException, self).__init__(*args)
