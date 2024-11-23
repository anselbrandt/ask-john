<script>
	let data = $state({});

	const handleClick = async () => {
		const res = await fetch('https://air.anselbrandt.net/api/kanye');
		data = await res.json();
	};
</script>

<button onclick={handleClick}> Click to Load Data </button>
<pre>
  {JSON.stringify(data, null, 2)}
</pre>
