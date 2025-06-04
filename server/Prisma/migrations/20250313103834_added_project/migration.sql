-- CreateTable
CREATE TABLE `project` (
    `id` VARCHAR(191) NOT NULL,
    `title` VARCHAR(25) NOT NULL,
    `description` VARCHAR(255) NOT NULL,
    `user_id` VARCHAR(191) NOT NULL,
    `deadline` DATETIME(3) NOT NULL,
    `created_at` TIMESTAMP(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0),
    `updated_at` TIMESTAMP(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0),

    INDEX `project_user_idx`(`user_id`),
    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
