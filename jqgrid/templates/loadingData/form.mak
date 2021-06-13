<form id="formLoadingData" action="${tg.url('/dataBase/save')}">
    <input hidden type="text" id="user_id_loading_data" value='${user_id}'>
    <fieldset>
        <legend>${_('User Data')} </legend>
        <table style="width:100%">
            <tr>
                <td>
                    ${_('User Name')}:
                </td>
                <td>
                    <input type="text" id="user_name_loading_data" name="user_name_loading_data" value='${user.user_name}'>
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
                    <input type="text" id="email_address_loading_data" name="email_address_loading_data" value='${user.email_address}'>
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
                    <input type="text" id="display_name_loading_data" name="display_name_loading_data" value='${user.display_name}'>
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
                    <input type="text" id="password_loading_data" name="password_loading_data" >
                </td>
            </tr>
        </table>
    </fieldset>
</form>