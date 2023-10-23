import { Platform } from '../types/parsed-types';
import { RawPlatform } from '../types/raw-types';

const IN_PROGRESS = 'in_progress';
const NOT_SUPPORTED = 'not_supported';
const DEPRECATED = 'deprecated';

export const parsePlatforms = (
    platforms: Record<string, RawPlatform>
): Record<string, Platform> => {
    const parsedPlatforms: Record<string, Platform> = {};
    Object.entries(platforms).forEach(([platformName, rawPlatform]) => {
        parsedPlatforms[platformName] = parsePlatform(rawPlatform, platformName);
    });

    return parsedPlatforms;
};

export const parsePlatform = (platform: RawPlatform, platformName: string): Platform => {
    const versions = String(platform.app_versions);
    if (versions !== NOT_SUPPORTED && versions !== DEPRECATED && !platform.ticket) {
        throw new Error(`No ticket attached for platform ${platformName}`);
    }
    const { firstVersion, lastVersion } = parseVersions(versions);
    return {
        name: platformName,
        firstVersion,
        lastVersion,
        ticket: platform.ticket,
    };
};

const parseVersions = (versions: string): { firstVersion: string; lastVersion: string | null } => {
    if (versions === IN_PROGRESS) {
        return {
            firstVersion: IN_PROGRESS,
            lastVersion: null,
        };
    }

    if (versions === NOT_SUPPORTED) {
        return {
            firstVersion: NOT_SUPPORTED,
            lastVersion: NOT_SUPPORTED,
        };
    }

    if (versions === DEPRECATED) {
        return {
            firstVersion: DEPRECATED,
            lastVersion: DEPRECATED,
        };
    }

    const versionFormatted = versions.replaceAll(' ', '');
    if (versionFormatted.includes('-')) {
        const [firstVersion, lastVersion] = versionFormatted.replaceAll(' ', '').split('-');
        return {
            firstVersion,
            lastVersion,
        };
    }

    return {
        firstVersion: versionFormatted,
        lastVersion: null,
    };
};
