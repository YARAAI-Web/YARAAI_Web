rule auto_rule_20250727021215_1158 {
  strings:
    $o0 = "phNewUSKey" wide ascii nocase
    $o1 = "DlgDirListComboBoxA" wide ascii nocase
    $o2 = "StrCatBuffW" wide ascii nocase
    $o3 = "AssocQueryStringByKeyW" wide ascii nocase
    $o4 = "nMinPos" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727021218_8964 {
  strings:
    $o0 = "GetMenuPosFromID" wide ascii nocase
    $o1 = "pszSubKey" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727021222_7144 {
  condition:
    auto_rule_20250727021215_1158 or auto_rule_20250727021218_8964
}