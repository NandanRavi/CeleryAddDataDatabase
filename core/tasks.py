from celery import shared_task # type: ignore
from .models import Books
import time


@shared_task
def update_books_ratings(start_id):
    print(start_id)
    total_count = Books.objects.count()
    ids = [start_id + 100 * i for i in range(total_count)]
    
    for id_ in ids:
        book = Books.objects.filter(id=id_).first()
        print(book)
        if book:
            ratings = [3, 6, 10]
            for i, rating in enumerate(ratings, start=1):
                book.rating = rating
                print(f"Updating rating for book ID {id_} to {rating}")
                book.save()
                time.sleep(10)
            # for i in range(1, 4):
            #     if i==1:
            #         book.rating = 3
            #         print(f"Updating rating for book ID {id_} to {3}")
            #         book.save()
            #         time.sleep(10)
            #     elif i==2:
            #         book.rating = 6
            #         print(f"Updating rating for book ID {id_} to {6}")
            #         book.save()
            #         time.sleep(10)
            #     elif i==3:
            #         book.rating = 10
            #         print(f"Updating rating for book ID {id_} to {10}")
            #         book.save()
            #         time.sleep(10)
    return f"Ratings updated for IDs: {ids}"



