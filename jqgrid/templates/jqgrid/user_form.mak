<form id="form${id}" action="${h.url()}${id}/save">
    <input hidden type="text" id="user_id_${id}"  name="user_id_${id}" value='${user_id}'>
    <fieldset>
        <legend>${_('User Data')} </legend>
        <table style="width:100%">
            <tr>
                <td>
                    ${_('User Name')}:
                </td>
                <td>
                    <input type="text" id="user_name_${id}" name="user_name_${id}" value='${user.user_name}'>
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
                    <input type="text" id="email_address_${id}" name="email_address_${id}" value='${user.email_address}'>
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
                    <input type="text" id="display_name_${id}" name="display_name_${id}" value='${user.display_name}'>
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
                    <input type="text" id="password_${id}" name="password_${id}" >
                </td>
            </tr>
        </table>
    </fieldset>
</form>