<script type="text/javascript">
	function check() {
		var username = document.getElementById("username").value;
		var email = document.getElementById("email").value;
		if(username==null || username==''){
			alert("�û�������Ϊ�գ����������룡����");
			return false; 
		}
		else if(!/^[a-z]+$/i.test(username)) {
			alert("������ֻ�ܰ���Ӣ����ĸ�����������룡����");
			return false;   					
		}
		else if(email==null || email==''){
			document.getElementById("id3").value="���䲻��Ϊ�գ����������룡����"
			alert("���䲻��Ϊ�գ����������룡����");
			return false; 
		}				
		else if(!/^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/.test(email)) {
			alert("�����ʽ����ȷ��" + "����������!!!");
			return false; 
		}
	}
	function checkLength(obj) {
		var maxChars = 20;//����ַ��� 
		var curr = maxChars - getByteLen(obj.value);
		if (curr > 0) {
			document.getElementById("checklen").innerHTML = curr.toString();
		} else {
			document.getElementById("checklen").innerHTML = '0';
			document.getElementById("subject").readOnly = true;
			}
		}
	
</script>