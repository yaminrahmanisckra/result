# PostgreSQL Setup Guide

এই গাইড আপনাকে SQLite থেকে PostgreSQL এ পরিবর্তন করতে সাহায্য করবে।

## প্রয়োজনীয়তা

1. PostgreSQL ইনস্টল করা থাকতে হবে
2. Python environment সেটআপ করা থাকতে হবে

## ধাপ ১: PostgreSQL ইনস্টল করা

### macOS এর জন্য:
```bash
brew install postgresql
brew services start postgresql
```

### Ubuntu/Debian এর জন্য:
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### Windows এর জন্য:
PostgreSQL এর অফিশিয়াল ওয়েবসাইট থেকে ডাউনলোড করুন।

## ধাপ ২: ডাটাবেস তৈরি করা

```bash
# PostgreSQL এ লগইন করুন
sudo -u postgres psql

# ডাটাবেস তৈরি করুন
CREATE DATABASE result_management;

# ইউজার তৈরি করুন (ঐচ্ছিক)
CREATE USER your_username WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE result_management TO your_username;

# PostgreSQL থেকে বের হন
\q
```

## ধাপ ৩: Environment Variables সেট করা

`.env` ফাইল তৈরি করুন (যদি না থাকে):

```env
# Flask Configuration
SECRET_KEY=your-secret-key-here

# PostgreSQL Database Configuration
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
DB_NAME=result_management
```

## ধাপ ৪: Dependencies ইনস্টল করা

```bash
pip install -r requirements.txt
```

## ধাপ ৫: ডাটাবেস টেবিল তৈরি করা

```bash
python setup_postgres.py
```

## ধাপ ৬: ডাটা মাইগ্রেট করা (ঐচ্ছিক)

যদি আপনার SQLite ডাটাবেসে ডাটা থাকে:

```bash
python migrate_db.py
```

## ধাপ ৭: অ্যাপ্লিকেশন টেস্ট করা

```bash
cd result_management
python app.py
```

## Production Deployment

### Render এর জন্য:

1. Render এ PostgreSQL সার্ভিস তৈরি করুন
2. Environment variables সেট করুন:
   - `DATABASE_URL`: Render এর PostgreSQL URL
   - `SECRET_KEY`: আপনার secret key

### Heroku এর জন্য:

1. Heroku PostgreSQL addon যোগ করুন:
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```

2. Environment variables সেট করুন:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   ```

## ট্রাবলশুটিং

### সাধারণ সমস্যা:

1. **Connection Error**: 
   - PostgreSQL সার্ভিস চালু আছে কিনা চেক করুন
   - Database credentials সঠিক কিনা চেক করুন

2. **Permission Error**:
   - Database user এর proper permissions আছে কিনা চেক করুন

3. **Port Error**:
   - PostgreSQL default port (5432) ব্যবহার করছে কিনা চেক করুন

### লগ চেক করা:

```bash
# PostgreSQL logs (Ubuntu/Debian)
sudo tail -f /var/log/postgresql/postgresql-*.log

# macOS
tail -f /usr/local/var/log/postgresql.log
```

## ডাটাবেস ব্যাকআপ

```bash
# Backup
pg_dump -U postgres result_management > backup.sql

# Restore
psql -U postgres result_management < backup.sql
``` 