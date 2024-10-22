<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>bbPress installer &rsaquo; Welcome</title>
	<meta name="robots" content="noindex, nofollow" />
	<link rel="stylesheet" href="/internal/bb-admin/install.css" type="text/css" />
</head>
<body>
	<div id="container">
		<div class="logo">
			<img src="/internal/bb-admin/images/bbpress-logo.png" alt="bbPress" />
		</div>
		<script type="text/javascript" charset="utf-8">
			function toggleNote(target) {
				var targetObj = document.getElementById(target);
				if (targetObj.style.display == 'none') {
					targetObj.style.display = 'block';
				} else {
					targetObj.style.display = 'none';
				}
			}
			function toggleBlock(toggleObj, target) {
				var targetObj = document.getElementById(target);
				if (toggleObj.checked) {
					targetObj.style.display = 'block';
				} else {
					targetObj.style.display = 'none';
				}
			}
			function toggleValue(toggleObj, target, offValue, onValue) {
				var targetObj = document.getElementById(target);
				if (toggleObj.checked) {
					targetObj.value = onValue;
				} else {
					targetObj.value = offValue;
				}
			}
		</script>
<div id="step0" class="open">
<h2 class="open">Welcome to the bbPress installer</h2>
<div>
<p class="intro">We're now going to go through a few steps to get you up and running.</p>
<p class="intro last">Ready? Then let's get started!</p>
				<form action="install.php" method="post">
<p class="message last">There doesn't seem to be a <code>bb-config.php</code> file. This usually means that you want to install bbPress.</p>
<fieldset class="buttons">
	<input type="hidden" id="step" name="step" value="1" />
	<label id="label-forward_0_0" for="forward_0_0" class="forward">
		<input type="submit" id="forward_0_0" name="forward_0_0" class="button" value="Go to step 1" tabindex="1" />
	</label>
</fieldset>
				</form>
</div></div>
<div id="step1" class="closed">
<h2 class="closed">Step 1 - Database configuration</h2>
<div>
</div></div>
<div id="step2" class="closed">
<h2 class="closed">Step 2 - WordPress integration (optional)</h2>
<div>
</div></div>
<div id="step3" class="closed">
<h2 class="closed">Step 3 - Site settings</h2>
<div>
</div></div>
	</div>
</body>
</html>

