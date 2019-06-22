def stats_handler(self, candidate, stats, message):
        now = int(time.time())
        print '@%d' % now, message.candidate.get_member().mid.encode('hex'), json.dumps(stats)

        candidate_mid = candidate.get_member().mid
        stats = self.preprocess_stats(stats)
        stats['time'] = now
        stats_old = self.crawl_message.get(candidate_mid, None)
        self.crawl_message[candidate_mid] = stats

        if stats_old is None:
            return

        time_dif = float(stats['uptime'] - stats_old['uptime'])
        if time_dif > 0:
            for index, key in enumerate(['bytes_orig', 'bytes_exit', 'bytes_relay']):
                self.current_stats[index] = self.current_stats[index] * 0.875 + \
                    (((stats[key] - stats_old[key]) / time_dif) / 1024) * 0.125 