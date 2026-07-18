-- Seed the admin.personalize privilege and grant it to admin-capable roles.
-- Idempotent: uses WHERE NOT EXISTS guards so re-running is safe.

-- 1. Create the privilege (fixed UUID so grants are deterministic)
INSERT INTO admin.privileges (privilege_id, module, action, description)
SELECT 'f1f1f1f1-0000-0000-0000-000000000001'::uuid,
       'admin', 'personalize',
       'Personalize UI layouts (admin management)'
WHERE NOT EXISTS (
    SELECT 1 FROM admin.privileges
    WHERE module = 'admin' AND action = 'personalize'
);

-- 2. Grant to Administrator and Manager roles (idempotent per role)
INSERT INTO admin.role_privileges (role_id, privilege_id)
SELECT r.role_id, 'f1f1f1f1-0000-0000-0000-000000000001'::uuid
FROM admin.roles r
WHERE r.role_name IN ('Administrator', 'Manager')
  AND NOT EXISTS (
    SELECT 1 FROM admin.role_privileges rp
    WHERE rp.role_id = r.role_id
      AND rp.privilege_id = 'f1f1f1f1-0000-0000-0000-000000000001'::uuid
  );

-- 3. Seed the admin.manage_profiles privilege (EBS User Profiles) + grant
INSERT INTO admin.privileges (privilege_id, module, action, description)
SELECT 'f1f1f1f1-0000-0000-0000-000000000002'::uuid,
       'admin', 'manage_profiles',
       'Manage user profile options (EBS-style)'
WHERE NOT EXISTS (
    SELECT 1 FROM admin.privileges
    WHERE module = 'admin' AND action = 'manage_profiles'
);

INSERT INTO admin.role_privileges (role_id, privilege_id)
SELECT r.role_id, 'f1f1f1f1-0000-0000-0000-000000000002'::uuid
FROM admin.roles r
WHERE r.role_name IN ('Administrator', 'Manager')
  AND NOT EXISTS (
    SELECT 1 FROM admin.role_privileges rp
    WHERE rp.role_id = r.role_id
      AND rp.privilege_id = 'f1f1f1f1-0000-0000-0000-000000000002'::uuid
  );
