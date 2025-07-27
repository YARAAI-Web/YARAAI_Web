rule auto_rule_20250726133959_9417 {
  strings:
    $o0 = "x43BDu" wide ascii nocase
    $o1 = "dword_409839" wide ascii nocase
    $o2 = "dword_4097BD" wide ascii nocase
    $o3 = "dword_4092E0" wide ascii nocase
    $o4 = "x818AF8" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726134002_6286 {
  strings:
    $o0 = "dword_4097E9" wide ascii nocase
    $o1 = "x7A40u" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726134006_7787 {
  condition:
    auto_rule_20250726133959_9417 or auto_rule_20250726134002_6286
}