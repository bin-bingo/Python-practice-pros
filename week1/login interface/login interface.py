#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-04 21:43:34
# @Author  : bin (binbingolj@gmail.com)
# @Link    : http://null
# @Version : $Id$

import os
import json
# all_users_data = {}
'''[summary]
all_users_data
               all_users list 存放所有用户名，用于检测是否存在
               user=[username,password,0/1]
[description]
'''
while True:
    print('Please sign in or sign up\n')
    login_user = input('username:')
    login_password = int(input('password:'))

    with open('user.json', 'r') as f:
        all_users_data = json.load(f)
        print(all_users_data)
    pass

    while all_users_data.__contains__(login_user):
        error = 0
        if all_users_data[login_user][2] == 1:
            print('your account has been locked!!!!')
            break
        elif login_password == all_users_data[login_user][1]:
            print('\nwelcome' + login_user + 'login...')
            break

            all_users_data[login_user][2] = 1
            with open('user.json', 'w') as f:
                json.dump(all_users_data, f)
        else:
            error += 1
            if error < 3:
                print('\nplease try again')
            else:
                all_users_data[login_user][2] = 1
                with open('user.json', 'w') as f:
                    json.dump(all_users_data, f)
                print('your account has been locked!!!!')
                break
    else:
        while True:
            pass
            ask_new = input('Do you want to sign up ?(y/n)\n')
            if ask_new == 'y':
                data_list = []
                new_user = input('Please input your infor:\nusername:')
                new_passwoed = int(input('password:'))
                data_list.append(new_user)
                data_list.append(new_passwoed)
                data_list.append(0)
                all_users_data[new_user] = data_list
                # filename = new_user+'.json'
                with open('user.json', 'w') as f:
                    json.dump(all_users_data, f)
                pass
                break
            elif ask_new == 'n':
                print('byebye !')
                break
            else:
                # ask_new = input('Do you want to sign up ?(y/n)')
                continue
pass
