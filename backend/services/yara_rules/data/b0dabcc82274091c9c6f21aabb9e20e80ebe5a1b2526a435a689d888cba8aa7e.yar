rule auto_rule_20250726133058_0072 {
  strings:
    $o0 = "dword_433723" wide ascii nocase
    $o1 = "dword_433767" wide ascii nocase
    $o2 = "off_413A5E" wide ascii nocase
    $o3 = "dword_43382B" wide ascii nocase
    $o4 = "xF89C8531" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726133101_3519 {
  strings:
    $o0 = "off_4337DB" wide ascii nocase
    $o1 = "ImageList_LoadImageW" wide ascii nocase
    $o2 = "off_413C66" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726133104_7962 {
  condition:
    auto_rule_20250726133058_0072 or auto_rule_20250726133101_3519
}