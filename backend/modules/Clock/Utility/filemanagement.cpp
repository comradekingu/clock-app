/*
 * Copyright (C) 2015 Canonical Ltd
 *
 * This file is part of Ubuntu Clock App
 *
 * Ubuntu Clock App is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 3 as
 * published by the Free Software Foundation.
 *
 * Ubuntu Clock App is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <QDir>
#include <QDebug>

#include "filemanagement.h"

FileManagement::FileManagement(QObject *parent):
    QObject(parent)
{
}

void FileManagement::deleteFile(const QString &dirName, const QString &fileName)
{
    QDir dir(dirName);

    // If directory doesn't exist, return
    if (!dir.exists())
    {
        qCritical("Directory %s doesn't exist", dirName);
        return;
    }

    dir.remove(fileName);
}
