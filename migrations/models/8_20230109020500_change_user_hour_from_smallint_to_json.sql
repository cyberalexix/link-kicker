-- upgrade --
ALTER TABLE "user" ALTER COLUMN "hour" TYPE JSONB USING json_build_array("hour");
-- downgrade --
ALTER TABLE "user" ALTER COLUMN "hour" TYPE SMALLINT USING NULLIF("hour"[0], 'null')::SMALLINT;
