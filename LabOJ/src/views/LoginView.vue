<template>
	<header class="login">
		<nav>
			<ul>
				<a href=""><li>学习</li></a>
				<a href=""><li>题库</li></a>
				<a href=""><li>竞赛</li></a>
				<a href=""><li>讨论</li></a>
			</ul>
			<div class="search">
				<input type="text" placeholder="搜索">
				<span class="iconfont icon-31sousuo"></span>
			</div>
		</nav>
	</header>
	<section>
		<div class="section">
			<h1>注册</h1>
			<div class="middle">
				<div class="phone">
					<label for="">
						<input type="text" placeholder="+86   输入手机号">
					</label>
				</div>
				<div class="yanzheng">
					<label for="">
						<input type="text" placeholder="获取验证码">
					</label>
				</div>
				<div class="denglu">登录/注册</div>
				<a href="">账号密码登录</a>
			</div>
		</div>
	</section>
	<footer>

	</footer>
</template>

<script>
	// localStorage.setItem('token', token)  // 令牌储存机制：存入本地，此处为示例
</script>

<style>
	* {
		margin: 0;
		padding: 0;
		box-sizing: border-box;
		list-style: none;
	}

  .login {
		width: 100%;
		height: 50px;
		/* background-color: aqua; */
	}

	nav {
		display: flex;
		justify-content: space-between;
		line-height: 50px;
	}

	input {
		height: 25px;
		margin-right: 20px;
	}

	ul {
		display: flex;
		width: 300px;
		height: 50px;
		line-height: 50px;
		/* background-color: pink; */
		justify-content: space-between;
		margin: 0 50px;
	}
	li {
		color: #5c5c5c;
	}

	section {
		height: 500px;
		background-color: #faf9f9;
		padding: 50px;
	}

	.section {
		width: 350px;
		height: 400px;
		margin: 0 auto;
		background-color: white;
		border-radius: 20px;
		box-shadow: 2px 2px 20px 2px #4e4e4e;
	}

	h1 {
		text-align: center;
		padding-top: 50px;
	}

	.phone input,
	.yanzheng input{
		width: 280px;
		height: 35px;
		border-radius: 5px;
		outline: none;
		border: 1px solid #5c5c5c;
		margin-left: 35px;
		margin-top: 30px;
		padding: 10px 10px;
	}

	.yanzheng input::-webkit-input-placeholder{
		text-align: right;
	}

	.denglu {
		width: 280px;
		height: 38px;
		border-radius: 5px;
		margin-left: 35px;
		margin-top: 30px;
		background-color: #242528;
		color: white;
		text-align: center;
		line-height: 38px;
	}

	.middle a {
		display: block;
		color: #262626bf;
		margin: 15px 35px;
	}

	footer {
		height: 200px;
		background-color: #242528;
	}
</style>