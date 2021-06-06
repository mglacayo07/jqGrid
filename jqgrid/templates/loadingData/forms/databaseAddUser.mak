<form id="formDataBase" action="${tg.url('/dataBase/save')}">
    <input hidden type="text" id="user_id_database" value='${user_id}'>
    <fieldset>
        <legend>${_('User Data')} </legend>
        <table style="width:100%">
            <tr>
                <td>
                    ${_('User Name')}:
                </td>
                <td>
                    <input type="text" id="user_name_database" name="user_name_database" value='${user.user_name}'>
                </td>
            </tr>
            <tr style="height: 10px">
                <td></td>
            </tr>
            <tr>
                <td>
                    ${_('Email Address')}:
                </td>
                <td>
                    <input type="text" id="email_address_database" name="email_address_database" value='${user.email_address}'>
                </td>
            </tr>
            <tr style="height: 10px">
                <td></td>
            </tr>
            <tr>
                <td>
                    ${_('Display Name')}:
                </td>
                <td>
                    <input type="text" id="display_name_database" name="display_name_database" value='${user.display_name}'>
                </td>
            </tr>
            <tr style="height: 10px">
                <td></td>
            </tr>
            <tr>
                <td>
                    ${_('Password')}:
                </td>
                <td>
                    <input type="text" id="password_database" name="password_database" >
                </td>
            </tr>
        </table>
    </fieldset>
</form>