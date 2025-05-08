import os
import tempfile
import subprocess
import shutil


def run_code_in_docker(language, code: str, input_data: str = ""):
    # 创建临时目录（确保父目录存在）
    os.makedirs("/root/tmp_code", exist_ok=True)
    temp_dir = tempfile.mkdtemp(dir="/root/tmp_code")

    try:
        # 定义文件名和运行命令
        filename = {
            "python": "main.py",
            "cpp": "main.cpp",
            "java": "Main.java"
        }[language]

        file_path = os.path.join(temp_dir, filename)

        # 写入代码文件
        with open(file_path, "w") as f:
            f.write(code)

        # 写入输入文件（如果存在输入）
        input_file = os.path.join(temp_dir, "input.txt")
        with open(input_file, "w") as f:
            f.write(input_data)

        # 设置权限（确保容器内可访问）
        os.chmod(file_path, 0o777)
        os.chmod(input_file, 0o777)
        os.chmod(temp_dir, 0o777)

        # Docker 容器映射
        container_map = {
            "python": "oj-docker-python-runner",
            "cpp": "oj-docker-cpp-runner",
            "java": "oj-docker-java-runner"
        }

        # 不同语言的运行命令
        run_cmd_map = {
            "python": ["python3", filename],
            "cpp": ["sh", "-c", f"g++ {filename} -o main.out && ./main.out"],
            "java": ["sh", "-c", f"javac {filename} && java Main"]
        }

        # 运行 Docker 容器
        output = subprocess.run(
            [
                "docker", "run", "--rm", "-i",
                "-v", f"{temp_dir}:/app", "-w", "/app",
                container_map[language],
                *run_cmd_map[language]  # 动态注入对应语言的命令
            ],
            input=input_data.encode(),  # 传入输入数据
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5
        )

        # 返回结果（解码二进制输出）
        return {
            "stdout": output.stdout.decode("utf-8", errors="replace").strip(),  # 要记得转码
            "stderr": output.stderr.decode("utf-8", errors="replace").strip(),
            "status": "success" if output.returncode == 0 else "error"
        }

    except subprocess.TimeoutExpired:
        return {"status": "timeout", "stdout": "", "stderr": "Time limit exceeded"}

    except Exception as e:
        return {"status": "error", "stdout": "", "stderr": str(e)}

    finally:
        # 确保清理临时目录
        shutil.rmtree(temp_dir, ignore_errors=True)