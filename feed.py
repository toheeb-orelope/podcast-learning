import yaml
import xml.etree.ElementTree as xmlTree

with open('feed.yaml', 'r') as file:
    yamlData = yaml.safe_load(file)

    rssElement = xmlTree.Element('rss', {
    'version':'2.0',
    'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content':'http://purl.org/rss/1.0/modules/content/'
    })
    
    channelElement = xmlTree.SubElement(rssElement, 'channel')

    xmlTree.SubElement(channelElement, 'title').text = yamlData['title']

    linkPrefix = yamlData['link']
    
    xmlTree.SubElement(channelElement, 'title').text = yamlData['title']
    xmlTree.SubElement(channelElement, 'format').text = yamlData['format']
    xmlTree.SubElement(channelElement, 'subtitle').text = yamlData['subtitle']
    xmlTree.SubElement(channelElement, 'itunes:author').text = yamlData['author']
    xmlTree.SubElement(channelElement, 'description').text = yamlData['description']
    xmlTree.SubElement(channelElement, 'itunes:image', {'href': linkPrefix + yamlData['image']})
    xmlTree.SubElement(channelElement, 'language').text = yamlData['language']
    xmlTree.SubElement(channelElement, 'link').text = linkPrefix
    
    xmlTree.SubElement(channelElement, 'itunes:category', {'text': linkPrefix + yamlData['category']})

    for item in yamlData['item']:
        itemElement = xmlTree.SubElement(channelElement, 'item')
        xmlTree.SubElement(channelElement, 'title').text = yamlData['title']
        xmlTree.SubElement(channelElement, 'itunes:author').text = yamlData['author']
        xmlTree.SubElement(channelElement, 'description').text = item['description']
        xmlTree.SubElement(channelElement, 'itunes:duration').text = item['duration']
        xmlTree.SubElement(channelElement, 'pubDate').text = item['published']
        xmlTree.SubElement(channelElement, 'title').text = item['title']

        enclosure = xmlTree.SubElement(itemElement, 'enclosure', {
            'url': linkPrefix + item['file'],
            'type': 'audio/mpeg',
            'length': item['length']
        })

    outputTree = xmlTree.ElementTree(rssElement)
    outputTree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)