#!/usr/bin/perl  
use CGI qw(:standard);
if(param('UserName') eq  "" || param('Name') eq "" || param('ConfPassword') eq "" || param('password') eq "" )
{
	print "Content-type: text/html\n\n";
	print <<'eof'
	<script language="JavaScript">
	alert("Please fill in all fields");
	history.go(-1);

	</script>
eof
}
elsif (!(param('password') eq  param('ConfPassword')))
{
	print "Content-type: text/html\n\n";
	print <<'eof'
	<script language="JavaScript">
	alert("Passwords do not Match!");
	history.go(-1);

	</script>
eof
}
else
{
	my %data= (
		Uname=>  param('UserName'),
		Fullname=>  param('Name'),
		password => param('password'),
	);
	open my $f2, "Members.csv" or die $!;
	my $bol =1;
	while (my $row = <$f2>)
	{
		my @values= split(',', $row);
		if ($values[0] eq $data{Uname})
		{
			$bol=0;
			print "Content-type: text/html\n\n";
			print <<'eof'
			<script language="JavaScript">
			alert("Username Already Exists");
			history.go(-1);
			</script>
eof

		}
	}
	close $f2;
	if ($bol==1)
	{
		open my $fh, ">>", "Members.csv" or die $!;
		print $fh "$data{Uname},";
		print $fh "$data{password},";
		print $fh "$data{Fullname}\n";
		print "Content-type: text/html\n\n";

		#print "$data{Fullname} ";
		#print "$data{Uname} ";
		#print "$data{password} ";
		#print "$data{Cpassword} ";
		print "Thank you for Registering!\n";
		print <<'eof' ;
		<HTML>

		<a href="index.html">  Click Here to go back to Home page</a>
		</HTML>
eof
	}
}
