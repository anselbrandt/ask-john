<script>
	import { page } from '$app/stores';
	import { base } from '$app/paths';
</script>

<header>
	<ul>
		<li aria-current={$page.url.pathname === '/app/' ? 'page' : undefined}>
			<a href="{base}/">Home</a>
		</li>
		<li aria-current={$page.url.pathname === '/app/images' ? 'page' : undefined}>
			<a href="{base}/images">Images</a>
		</li>
		<li aria-current={$page.url.pathname === '/app/chuck' ? 'page' : undefined}>
			<a href="{base}/chuck">Chuck Norris</a>
		</li>
		<li aria-current={$page.url.pathname === '/app/kanye' ? 'page' : undefined}>
			<a href="{base}/kanye">Kanye</a>
		</li>
	</ul>
</header>
