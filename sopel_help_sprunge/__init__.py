from sopel_help.providers import AbstractPublisher, _post_content

class SprungePublisher(AbstractPublisher):
    """Publishing provider using sprunge.us"""
    def publish(self, bot, trigger, content):
        response = _post_content('http://sprunge.us/', data={
            'sprunge': content
        })
        return response.text.strip()
