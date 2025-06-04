-- CreateTable
CREATE TABLE `user` (
    `id` VARCHAR(191) NOT NULL,
    `full_name` VARCHAR(120) NOT NULL,
    `username` VARCHAR(120) NOT NULL,
    `email` VARCHAR(120) NOT NULL,
    `status` ENUM('active', 'inactive') NOT NULL DEFAULT 'active',
    `role` ENUM('admin', 'member', 'moderator') NOT NULL DEFAULT 'member',
    `password` VARCHAR(255) NOT NULL,
    `created_at` TIMESTAMP(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0),
    `updated_at` TIMESTAMP(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0),

    UNIQUE INDEX `user_email_UNIQUE`(`email`),
    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
