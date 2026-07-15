CREATE TABLE admin.objects (
    object_id UUID DEFAULT uuidv7() NOT NULL PRIMARY KEY,
    object_type VARCHAR(50) NOT NULL,
    module_name VARCHAR(100),
    object_name VARCHAR(255) NOT NULL,
    parent_object_id UUID REFERENCES admin.objects(object_id),
    description TEXT,
    metadata JSONB,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

CREATE INDEX ix_objects_type ON admin.objects(object_type);
CREATE INDEX ix_objects_module ON admin.objects(module_name);
CREATE INDEX ix_objects_parent ON admin.objects(parent_object_id);
