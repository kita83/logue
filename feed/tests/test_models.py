"""feedアプリのModelテスト"""
import feedparser
from django.test import TestCase
from feed.models import Channel, Episode, Subscription
from accounts.models import LogueUser
from feed import views, utils


class ChannelModelTest(TestCase):
    """
    チャンネルモデル
    """
    def test_is_empty(self):
        saved_channels = Channel.objects.all()
        self.assertEqual(saved_channels.count(), 0)

    def test_save(self):
        """
        チャンネルの新規登録ができる
        """
        feed_url = 'http://feeds.rebuild.fm/rebuildfm'
        feeds = feedparser.parse(feed_url)
        ch = feeds.channel

        utils.save_channel(ch, feed_url)
        c = Channel.objects.get(title='Rebuild')
        actual = c.link
        self.assertEqual(actual, 'http://rebuild.fm')

    def test_did_not_save(self):
        """
        チャンネル情報に不備がある場合に登録されない
        """
        feed_url = 'http://feeds.test.fm/testfm'
        ch = None
        utils.save_channel(ch, feed_url)
        actual = Channel.objects.filter(feed_url='http://feeds.test.fm/testfm')
        self.assertEqual(actual.count(), 0)


class EpisodeModelTest(TestCase):
    """
    エピソードモデル
    """
    def test_save(self):
        """
        エピソードの新規登録ができる
        """
        Channel.objects.create(
            title='test_title',
            description='description',
            link='http://test.fm',
            feed_url='http://podcast.1242.com/sand/index.xml',
            author_name='test_author',
            cover_image='images/3aff6b6927bd46a289f39ba2e77a2b5e.png'
        )

        feed_url = 'http://podcast.1242.com/sand/index.xml'
        feeds = feedparser.parse(feed_url)
        entries = feeds.entries

        exist_ch = Channel.objects.filter(feed_url=feed_url)
        utils.save_episode(exist_ch[0], entries)
        actual = Episode.objects.filter(channel=exist_ch[0])
        self.assertNotEqual(actual.count(), 0)


class SubscriptionModelTest(TestCase):
    """
    購読モデル
    """
    def test_save(self):
        """
        購読情報の新規登録ができる
        """
        feed_url = 'http://feeds.rebuild.fm/rebuildfm'
        feeds = feedparser.parse(feed_url)
        ch = feeds.channel

        user = LogueUser.objects.create(email='test@email.com', password='testpass')

        utils.save_channel(ch, feed_url)
        c = Channel.objects.get(title='Rebuild')
        utils.save_subscription(c, user)
        sub = Subscription.objects.get(user=user)
        actual = sub.user.email
        self.assertEqual(actual, 'test@email.com')
