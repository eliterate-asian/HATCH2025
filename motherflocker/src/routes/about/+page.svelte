<script lang="ts">
	import { goto } from '$app/navigation';

	function goTo() {
		goto('register');
	}
</script>


<h1>Mother Flocker</h1>
<h2>Release 0.1</h2>
<p>A regional database and disease tracker for the risk assessment of avian-flu affected areas.</p>
<button on:click={goTo}>TAKE ME AWAY TO REGISTRY</button>