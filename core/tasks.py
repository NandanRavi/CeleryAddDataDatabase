from celery import shared_task # type: ignore
import time
from .models import Books

@shared_task
def update_books_ratings(start_id):
    print("start_id={}".format(start_id))

    total_count = Books.objects.count()
    ids = [start_id + 100 * i for i in range(1)]
    print(ids)
    for id_ in ids:
        for i in range(1, 4):
            for j in range(0, 5):
                counter = 100 * j
                book_id = id_ + counter
                book = Books.objects.filter(id=book_id).first()

                if book:
                    if i == 1:
                        book.rating = 3
                    elif i == 2:
                        book.rating = 6
                    elif i == 3:
                        book.rating = 10
                    
                    book.save()
                    print(f"Updated rating for book ID {book_id} to {book.rating}")
            time.sleep(5)
    # id_ += 500

    return f"Ratings updated for IDs: {ids}"


