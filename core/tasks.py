from celery import shared_task # type: ignore
import time
from .models import Books

@shared_task
def update_books_ratings(start_id):
    print("start_id={}".format(start_id))

    total_count = Books.objects.count()
    ids = [start_id + 100 * i for i in range(2)]
    print(ids)
    for id_ in range(start_id, ids[-1] + 1, 500):
        # print("id_")
        # print(id_)
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

            time.sleep(10)
            print('\n')
    id_ += 500

    return f"Ratings updated for IDs: {ids}"



# @shared_task
# def update_books_ratings(start_id):
#     print(start_id)
#     total_count = Books.objects.count()
#     ids = [start_id + 100 * i for i in range(total_count)]
#     for id_ in ids:
#         print(id_)
#         book = Books.objects.filter(id=id_).first()
#         print(book)
#         if book:
#             for i in range(1, 4):
#                 for j in range(0, 5):
#                     counter = 100*j
#                     if i==1:
#                         book.rating = 3
#                         print(f"Updating rating for book ID {id_+counter} to {1}")
#                         book.save()
#                     elif i==2:
#                         book.rating = 6
#                         print(f"Updating rating for book ID {id_+counter} to {2}")
#                         book.save()
#                     elif i==3:
#                         book.rating = 10
#                         print(f"Updating rating for book ID {id_+counter} to {3}")
#                         book.save()
#                     print("\n")
#                 time.sleep(2)
#     return f"Ratings updated for IDs: {ids}"

#             # ratings = [3, 6, 10]
#             # for i, rating in enumerate(ratings, start=1):
#             #     book.rating = rating
#             #     print(f"Updating rating for book ID {id_} to {rating}")
#             #     book.save()
#             #     time.sleep(10)

