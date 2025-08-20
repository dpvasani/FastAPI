import {themes as prismThemes} from 'prism-react-renderer';
import path from 'path';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'FastAPI Documentation',
  tagline: 'Complete FastAPI Guide & Best Practices',
  favicon: 'img/logo.svg',

  // Set the production url of your site here
  url: 'https://your-username.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  baseUrl: '/',

  // GitHub pages deployment config.
  organizationName: 'your-username',
  projectName: 'fastapi-docs',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: '../Blogs',
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/your-username/fastapi-docs/tree/main/',
          showLastUpdateTime: true,
          showLastUpdateAuthor: true,
          routeBasePath: 'docs',
          include: ['**/*.md', '**/*.mdx']
          ,
          // Display labels using the actual file names (keep numeric prefixes like "1. ")
          sidebarItemsGenerator: async function sidebarItemsGenerator({defaultSidebarItemsGenerator, ...args}) {
            const sidebarItems = await defaultSidebarItemsGenerator(args);
            const docById = Object.fromEntries(
              args.docs.map((d) => [d.id, d])
            );

            function mapItems(items: any[]): any[] {
              return items.map((item) => {
                if (item.type === 'category' && Array.isArray(item.items)) {
                  return { ...item, items: mapItems(item.items) };
                }
                if (item.type === 'doc' && docById[item.id]?.source) {
                  const sourcePath = docById[item.id].source as string;
                  const base = path.basename(sourcePath).replace(/\.(md|mdx)$/i, '');
                  return { ...item, label: base };
                }
                return item;
              });
            }

            return mapItems(sidebarItems);
          }
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/your-username/fastapi-docs/tree/main/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    mermaid: {
      theme: { light: 'neutral', dark: 'dark' }
    },
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'FastAPI Docs',
      logo: {
        alt: 'FastAPI Logo',
        src: 'img/logo.svg',
        srcDark: 'img/logo-dark.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Docs',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/your-username/fastapi-docs',
          label: 'GitHub',
          position: 'right',
        },
        {
          type: 'html',
          position: 'right',
          value: '<a href="/about" class="navbar__link">About</a>',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: '/docs/get-methods',
            },
            {
              label: 'API Reference',
              to: '/docs/routing',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/your-username',
            },
            {
              label: 'LinkedIn',
              href: 'https://linkedin.com/in/your-username',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/your-username',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'YouTube',
              href: 'https://youtube.com/@your-channel',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} FastAPI Documentation. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['python', 'bash', 'json'],
    },
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    // Algolia disabled; using local search plugin instead
  } satisfies Preset.ThemeConfig,
  themes: ['@docusaurus/theme-mermaid'],
  markdown: {
    mermaid: true
  },
  plugins: [
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {
        hashed: true,
        indexDocs: true,
        indexBlog: true,
        docsRouteBasePath: '/docs',
        blogRouteBasePath: '/blog',
        language: ['en']
      }
    ]
  ],
};

export default config;