<?php
/**
 * Settings → The Roof Crew.
 * Where quote requests go, how they're sent, test mode (noindex) and an optional staging lock.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

function rc_setting_defaults() {
	return array(
		'enquiry_email' => 'mike@theroofcrew.co.nz',
		'from_email'    => '',
		'resend_key'    => '',
		'test_mode'     => 1,
		'login_lock'    => 0,
	);
}

function rc_setting( $key ) {
	$all = wp_parse_args( (array) get_option( 'rc_settings', array() ), rc_setting_defaults() );
	return isset( $all[ $key ] ) ? $all[ $key ] : null;
}

add_action( 'admin_init', function () {
	register_setting( 'rc_settings', 'rc_settings', array(
		'type'              => 'array',
		'sanitize_callback' => function ( $in ) {
			$in  = (array) $in;
			$old = (array) get_option( 'rc_settings', array() );
			$key = isset( $in['resend_key'] ) ? trim( sanitize_text_field( $in['resend_key'] ) ) : '';
			return array(
				'enquiry_email' => sanitize_email( isset( $in['enquiry_email'] ) ? $in['enquiry_email'] : '' ),
				'from_email'    => sanitize_email( isset( $in['from_email'] ) ? $in['from_email'] : '' ),
				// The key field is left blank on screen; blank means "keep the saved key".
				'resend_key'    => ! empty( $in['resend_key_clear'] ) ? '' : ( '' !== $key ? $key : ( isset( $old['resend_key'] ) ? $old['resend_key'] : '' ) ),
				'test_mode'     => empty( $in['test_mode'] ) ? 0 : 1,
				'login_lock'    => empty( $in['login_lock'] ) ? 0 : 1,
			);
		},
	) );
} );

add_action( 'admin_menu', function () {
	add_options_page( 'The Roof Crew', 'The Roof Crew', 'manage_options', 'rc-settings', 'rc_settings_page' );
} );

function rc_settings_page() {
	$s = wp_parse_args( (array) get_option( 'rc_settings', array() ), rc_setting_defaults() );
	?>
	<div class="wrap">
		<h1>The Roof Crew</h1>
		<?php if ( isset( $_GET['rc_setup'] ) ) : // phpcs:ignore ?>
			<div class="notice notice-success"><p><?php echo esc_html( sanitize_text_field( wp_unslash( $_GET['rc_setup'] ) ) ); // phpcs:ignore ?></p></div>
		<?php endif; ?>
		<form method="post" action="options.php">
			<?php settings_fields( 'rc_settings' ); ?>
			<table class="form-table" role="presentation">
				<tr><th scope="row"><label for="rc-email">Send quote requests to</label></th>
					<td><input id="rc-email" class="regular-text" type="email" name="rc_settings[enquiry_email]" value="<?php echo esc_attr( $s['enquiry_email'] ); ?>">
					<p class="description">Every quote request is emailed here and also saved under <strong>Quote requests</strong> in the sidebar, so nothing is lost if an email goes astray.</p></td></tr>
				<tr><th scope="row"><label for="rc-from">Send from</label></th>
					<td><input id="rc-from" class="regular-text" type="email" name="rc_settings[from_email]" value="<?php echo esc_attr( $s['from_email'] ); ?>" placeholder="website@theroofcrew.co.nz">
					<p class="description">Optional. An address on the website's own domain is least likely to land in spam. Replies always go to the customer.</p></td></tr>
				<tr><th scope="row"><label for="rc-resend">Resend API key</label></th>
					<td><input id="rc-resend" class="regular-text" type="password" autocomplete="off" name="rc_settings[resend_key]" value="" placeholder="<?php echo $s['resend_key'] ? esc_attr__( 'Saved (leave blank to keep)', 'roofcrew' ) : 're_...'; ?>">
					<?php if ( $s['resend_key'] ) : ?><label style="margin-left:8px"><input type="checkbox" name="rc_settings[resend_key_clear]" value="1"> Remove saved key</label><?php endif; ?>
					<p class="description">Optional. With a key, quote requests are sent through Resend (more reliable delivery). Without one, WordPress sends them the normal way. The "Send from" address must be on a domain verified in Resend.</p></td></tr>
				<tr><th scope="row">Test mode</th>
					<td><label><input type="checkbox" name="rc_settings[test_mode]" value="1" <?php checked( $s['test_mode'], 1 ); ?>> Hide the site from search engines</label>
					<p class="description">Untick this on launch day.</p></td></tr>
				<tr><th scope="row">Staging lock</th>
					<td><label><input type="checkbox" name="rc_settings[login_lock]" value="1" <?php checked( $s['login_lock'], 1 ); ?>> Only logged-in users can see the site</label>
					<p class="description">For a staging copy. Never tick this on the live site.</p></td></tr>
			</table>
			<?php submit_button(); ?>
		</form>

		<hr>
		<h2>Starter content</h2>
		<p>Creates the pages (Home, About, Contact, Free quote, Services with its 5 service pages, Locations with its 4 area pages), sets Home as the front page and switches links to the "Post name" style. Reroofing and East Auckland are published; the other services and areas are created as drafts to fill in and publish. Safe to run more than once: pages that already exist are kept.</p>
		<form method="post" action="<?php echo esc_url( admin_url( 'admin-post.php' ) ); ?>">
			<input type="hidden" name="action" value="rc_setup_content">
			<?php wp_nonce_field( 'rc_setup_content' ); ?>
			<?php submit_button( 'Import starter content', 'secondary', 'submit', false ); ?>
		</form>
	</div>
	<?php
}

/* Test mode: noindex. */
add_filter( 'wp_robots', function ( $robots ) {
	if ( rc_setting( 'test_mode' ) ) {
		$robots['noindex']  = true;
		$robots['nofollow'] = true;
	}
	return $robots;
} );

/* Staging lock: send logged-out visitors to the login screen. */
add_action( 'template_redirect', function () {
	if ( rc_setting( 'login_lock' ) && ! is_user_logged_in() ) {
		auth_redirect();
	}
} );
