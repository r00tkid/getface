<script>
    import {Line} from 'vue-chartjs'

    export default {
        name: 'Chart',
        extends: Line,
        props: {
            chart_data: {
                type: Object,
                default: null
            },
            chart_options: {
                type: Object,
                default: null
            },
            chart_render: {
                type: Boolean,
                default: true,
            }
        },
        methods: {
            selfRender(is_render) {
                if (is_render) this.renderChart(this.chart_data, this.chart_options);
            }
        },
        mounted() {
            this.selfRender(true);
        },
        watch: {
            chart_render: function (is_render) {
                this.selfRender(is_render);
            }
        }
    }
</script>
