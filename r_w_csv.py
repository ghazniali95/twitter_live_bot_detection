class CSV:
    def read(self, link, mode):
        try:
            file = open(link, mode)
        except:
            print "File does not exist please specify proper file path : Use full path starting from C:/dir/dir...."
        try:
            data = file.read()
            data2 = data.split('\n')
            final_data = []
            for d in data2:
                final_data.append(d.split(","))
            return final_data
        except:
            print "Software only Supports CSV File.";