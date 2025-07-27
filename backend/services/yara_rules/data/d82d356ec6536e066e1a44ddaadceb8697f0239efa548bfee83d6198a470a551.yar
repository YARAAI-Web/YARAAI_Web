rule auto_rule_20250726142134_8921 {
  strings:
    $o0 = "load_config_used" wide ascii nocase
    $o1 = "_raise_securityfailure" wide ascii nocase
    $o2 = "byte_140004601" wide ascii nocase
    $o3 = "register_onexit_function" wide ascii nocase
    $o4 = "qword_140003248" wide ascii nocase
  condition:
    4 of ($o*)
}