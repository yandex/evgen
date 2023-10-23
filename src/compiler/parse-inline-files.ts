import { resolve } from 'path';

const START_INLINE_FILE_TAG = '#start-file:';
const END_INLINE_FILE_TAG = '#end-file';

export const parseInlineFiles = (str: string, initialFile: string) => {
    const rows = str.split('\n');
    const filestack = [initialFile];
    const rowsByFile: Record<string, string> = {};
    for (let i = 0; i < rows.length; i += 1) {
        if (rows[i].startsWith(START_INLINE_FILE_TAG)) {
            const newFile = resolve(initialFile, '..', rows[i].split(START_INLINE_FILE_TAG)[1]);
            filestack.push(newFile);
        } else if (rows[i].startsWith(END_INLINE_FILE_TAG)) {
            filestack.pop();
        } else {
            const currentFile = filestack[filestack.length - 1];
            if (!rowsByFile[currentFile]) {
                rowsByFile[currentFile] = '';
            }

            const separator = rowsByFile[currentFile].length ? '\n' : '';
            rowsByFile[currentFile] += `${separator}${rows[i]}`;
        }
    }

    return rowsByFile;
};
