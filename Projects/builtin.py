# -*- coding: UTF-8 -*-

import os
import sys
import math
import platform

def save_builtin_versions(filename):
    with open(filename, 'w') as f:
        # 파이썬 버전
        f.write(f"Python version=={platform.python_version()}\n")
        
        # 내장 모듈과 버전 목록 작성
        modules = [os, math, sys]  # 필요한 다른 내장 모듈들도 추가해주세요
        for module in modules:
            try:
                module_name = module.__name__
                module_version = module.__version__
                f.write(f"{module_name}=={module_version}")
            except AttributeError:
                f.write(f"{module_name}==N/A")
            
            f.write("\n")

# 함수 호출하여 버전 정보를 builtin.txt 파일에 저장
save_builtin_versions('builtin.txt')