<template>
    <v-footer :fixed="true" app class="abn-footer">
        <span>GetFace &copy; {{ currentYear === 2018 ? currentYear : `2018 - ${currentYear}` }}</span>
        <span class="abn-versions">
            <table style="border-collapse: collapse">
                <tbody>
                    <tr>
                        <td>front:&nbsp;</td>
                        <td>{{ build.front }}</td>
                    </tr>
                    <tr>
                        <td>back:&nbsp;</td>
                        <td>{{ build.back }}</td>
                    </tr>
                    <tr>
                        <td>build:&nbsp;</td>
                        <td>{{ build.build }}</td>
                    </tr>
                </tbody>
            </table>
        </span>
    </v-footer>
</template>

<script>
    export default {
        name: "abn-footer",
        data: function () {
            return {
                currentYear: new Date().getFullYear(),
                build: this.versions,
            };
        },
    }
</script>

<style scoped>
    .abn-footer {
        display: flex;
        flex-flow: row nowrap;
        justify-content: center;
        align-content: center;
    }

    .abn-versions {
        position: absolute;
        right: 1px;
        bottom: 1px;
        font-size: 4px;
        line-height: 4px;
    }
</style>