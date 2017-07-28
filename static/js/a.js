<script type="text/javascript">
	function check() {
		var username = document.getElementById("username").value;
		var email = document.getElementById("email").value;
		if(username==null || username==''){
			alert("用户名不能为空，请重新输入！！！");
			return false; 
		}
		else if(!/^[a-z]+$/i.test(username)) {
			alert("姓名中只能包含英文字母，请重新输入！！！");
			return false;   					
		}
		else if(email==null || email==''){
			document.getElementById("id3").value="邮箱不能为空，请重新输入！！！"
			alert("邮箱不能为空，请重新输入！！！");
			return false; 
		}				
		else if(!/^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/.test(email)) {
			alert("邮箱格式不正确，" + "请重新输入!!!");
			return false; 
		}
	}
	function checkLength(obj) {
		var maxChars = 20;//最多字符数 
		var curr = maxChars - getByteLen(obj.value);
		if (curr > 0) {
			document.getElementById("checklen").innerHTML = curr.toString();
		} else {
			document.getElementById("checklen").innerHTML = '0';
			document.getElementById("subject").readOnly = true;
			}
		}
	
</script>