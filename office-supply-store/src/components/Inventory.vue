<!-- <template>
    <div>
      <h1 class="title">Inventory List</h1>
      <ul1>
        <li>Desk</li>
        <li>Chair</li>
        <li>Pencils</li>
        <li>Pens</li>
      </ul1>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Inventory'
  }
  </script>
  
  <style>
  .title {
    font-size: 2em;
    text-align: center;
    margin-bottom: 1em;
  }
  ul1 {
  text-align: center;
  list-style: none;
  font-size: 20px;
}

  </style> -->

  <template>
    <div>
      <h1 class="title">Inventory List</h1>
      <ul>
        <li v-for="(item, index) in inventory" :key="index">
          {{ item.name }} - Stock: {{ item.stock }} - Price: {{ item.price }}
          <img v-if="item.name === 'Pencils'" :src="require(`@/assets/OfficePencil1.jpg`)" alt="Pencil Image" height="100" />
          <img v-if="item.name === 'Chair'" :src="require(`@/assets/OfficeChair1.jpg`)" alt="Chair Image" height="100" />
          <img v-if="item.name === 'Pens'" :src="require(`@/assets/OfficePen1.jpg`)" alt="Pen Image" height="100" />
          <img v-if="item.name === 'Desk'" :src="require(`@/assets/OfficeDesk1.jpg`)" alt="Desk Image" height="100" />
          <button v-if="item.stock > 0" @click="buyItem(index)">Add to Cart</button>
        </li>
      </ul>
    </div>
  </template>

<script>
export default {
  name: 'Inventory',
  data() {
    return {
      inventory: [
        { name: 'Desk', stock: 5, price: 50 },
        { name: 'Chair', stock: 10, price: 20 },
        { name: 'Pencils', stock: 20, price: 1 },
        { name: 'Pens', stock: 15, price: 2 }
      ]
    }
  },
  methods: {
    buyItem(index) {
      if (this.inventory[index].stock > 0) {
        this.inventory[index].stock--
      }
    }
  }
}
</script>
<style>
.title {
  font-size: 2em;
  text-align: center;
  margin-bottom: 1em;
}
ul {
  text-align: center;
  font-size: 20px;
  padding: 0;
  list-style: none; /* remove bullets */
}
li {
  margin-bottom: 0.5em;
}
</style>