tacklets.project - project management, issue tracking and wiki system
=====================================================================

Plug in
-------

To plug in the components of tackle.project, make sure `Tacklets`
package installed in your python virtual environment and then
add follow line into `site.zcml` of your tackle instance::

  <include package="tacklets.project" />

That's it.

Configure
---------

1. Add project in `Contents` system settings.

2. Configure access to the project, in `Security` system settings. See `Security` section.

3. Enjoy o_O

Security
--------

This tacklet provides 3 specific roles:

- `Project member` - able to create and manage documents;
- `Project watcher` - only able to see workflow state in addition to view documents;
- `Project customer` - able to create issues and abolish issue from `feedback` state;
- `Project supervisor` - able to close issues (verify, reject), and restore them, set responsibility.

And still important basic roles from Tackle CMS::

- `Viewer` - able to view documents

Member is role necessary to appear user name in "Responsible"
select box.

Watcher role useful if you configure security settings to make
able to see documents for non-members, for example for `Unauthenticated Users`
group (i.e. anonymouses). In this case you setup `Viewer` role for
them, but not `Project watcher`. This means they see documents but
can't see the workflow states.

Customer and Supervisor role names are self-explainable.
