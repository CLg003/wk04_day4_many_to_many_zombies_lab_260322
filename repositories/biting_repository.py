from controllers.zombie_types_controller import zombie_types
from db.run_sql import run_sql
from models.biting import Biting

import repositories.human_repository as human_repository
import repositories.zombie_repository as zombie_repository

def save(biting):
    sql = "INSERT INTO bitings (human_id, zombie_id) VALUES (%s, %s) RETURNING id"
    values = [biting.human.id, biting.zombie.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    biting.id = id

def select_all():
    bitings = []
    sql = "SELECT * FROM bitings"
    results = run_sql(sql)
    for row in results:
        human = human_repository.select(row['human_id'])
        zombie = zombie_repository.select(row['zombie_id'])
        biting = Biting(human, zombie, row['id'])
        bitings.append(biting)
    return bitings

def select(id):
    sql = "SELECT * FROM bitings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    human = human_repository.select(result['human_id'])
    zombie = zombie_repository.select(result['zombie_id'])
    biting = Biting(human, zombie, result['id'])
    return biting

def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)