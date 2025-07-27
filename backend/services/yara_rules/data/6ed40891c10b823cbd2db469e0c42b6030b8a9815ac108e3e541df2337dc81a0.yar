rule auto_rule_20250727035904_6961 {
  strings:
    $o0 = "dword_43B4DB" wide ascii nocase
    $o1 = "dword_43B063" wide ascii nocase
    $o2 = "dword_43B4D6" wide ascii nocase
    $o3 = "dword_444071" wide ascii nocase
    $o4 = "dword_43B436" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727035908_6766 {
  strings:
    $o0 = "aFsvbtckwrczpwk" wide ascii nocase
    $o1 = "dword_43B542" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727035913_6888 {
  condition:
    auto_rule_20250727035904_6961 or auto_rule_20250727035908_6766
}